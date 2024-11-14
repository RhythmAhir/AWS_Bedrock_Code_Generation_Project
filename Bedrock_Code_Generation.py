import boto3
import botocore.config
import json
from datetime import datetime


# Function to generate code based on user-provided instructions and language using Amazon Bedrock
def generate_code_using_bedrock(message: str, language: str) -> str:
    # Prepare the prompt to guide the language model in generating code
    prompt_text = f"""Human: Write {language} code for the following instructions: {message}.
    Assistant:
    """

    # Define the parameters for the model's response generation
    body = {
        "prompt": prompt_text,
        "max_tokens_to_sample": 2048,  # Limits the length of generated code
        "temperature": 0.1,  # Controls randomness; lower for deterministic output
        "top_k": 250,  # Top-k sampling for token selection
        "top_p": 0.2,  # Cumulative probability sampling for token selection
        "stop_sequences": ["\n\nHuman:"]  # Sequence to stop generation
    }

    try:
        # Initialize Bedrock client with specified region and timeout settings
        bedrock = boto3.client("bedrock-runtime", region_name="us-east-1",
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))

        # Send the request to the Bedrock model and get the response
        response = bedrock.invoke_model(body=json.dumps(body), modelId="anthropic.claude-v2")

        # Extract and decode the model's generated response
        response_content = response.get('body').read().decode('utf-8')
        response_data = json.loads(response_content)
        code = response_data["completion"].strip()  # Clean up whitespace
        return code

    except Exception as e:
        print(f"Error generating the code: {e}")  # Log any errors encountered
        return ""


# Function to save generated code to an S3 bucket
def save_code_to_s3_bucket(code, s3_bucket, s3_key):
    # Initialize S3 client
    s3 = boto3.client('s3')

    try:
        # Upload the code to the specified S3 bucket and key
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=code)
        print("Code saved to S3")  # Confirm successful save

    except Exception as e:
        print("Error when saving the code to S3")  # Log any errors


# Lambda handler function to process API Gateway events and handle the code generation workflow
def lambda_handler(event, context):
    # Parse the incoming JSON event data
    event = json.loads(event['body'])
    message = event['message']  # User's instructions for code generation
    language = event['key']  # Programming language specified by the user
    print(message, language)

    # Generate code using Bedrock based on the event data
    generated_code = generate_code_using_bedrock(message, language)

    # If code was successfully generated, save it to S3 with a unique key
    if generated_code:
        current_time = datetime.now().strftime('%H%M%S')  # Generate unique timestamped key
        s3_key = f'code-output/{message}.py'
        s3_bucket = 'bedrock-code-generation-project'

        # Save the generated code to the S3 bucket
        save_code_to_s3_bucket(generated_code, s3_bucket, s3_key)
    else:
        print("No code was generated")  # Notify if generation failed

    # Return success response to API Gateway
    return {
        'statusCode': 200,
        'body': json.dumps('Code generation complete')
    }
