# Project Report: Code Generation System with AWS Lambda, Bedrock, API Gateway, and Amazon S3

---

## 1. Introduction

In this project, I built a serverless solution to generate code snippets based on user-provided instructions. Using **AWS Lambda** as the processing engine, I integrated with **AWS Bedrock** to leverage the foundational model **Anthropic Claude-v2** for natural language processing. This setup is accessed via **API Gateway**, allowing users to submit requests using tools like Postman, and the generated code is stored in an **S3 bucket** for easy retrieval.

---

## 2. **Creating the AWS Lambda Function**

The **AWS Lambda function** serves as the core of my code generation process. It utilizes **AWS Bedrock** to generate code based on user instructions, stores the generated code in an **S3 bucket**, and is accessible through **API Gateway** for external requests.

### Key Components of the Lambda Function

- **Code Generation with Bedrock**:  
  I implemented the `generate_code_using_bedrock` function, which prepares a prompt based on the user’s request, specifying the programming language and instructions. This prompt is sent to Bedrock's **"Anthropic Claude-v2"** model for processing.

- **Storing Code in S3**:  
  I used the `save_code_to_s3_bucket` function to save the generated code in a specified **S3 bucket** with a unique key. Each file is saved in the `code-output` folder within the bucket, using a timestamped filename for easy tracking and retrieval.

- **Lambda Handler**:  
  The `lambda_handler` function receives **API Gateway** requests, parses the JSON payload, calls the code generation function, and stores the output in S3 upon successful execution. It then returns a successful response to the API Gateway.

The complete code for this Lambda function can be found in the **`Bedrock_Code_Generation.py`** file.

**Screenshot of the Lambda function code configuration**:  

![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/1.%20Lambda%20Function.png>)
---

## 3. Configuring Bedrock Integration

Inside the Lambda function code, I integrated AWS Bedrock to use the **"Anthropic Claude-v2"** model for generating code based on user prompts.

- **Prompt Configuration**:  
  I designed the prompt to instruct the model on what language to use and what code to write based on user-supplied instructions. Parameters like `temperature`, `max_tokens_to_sample`, and `stop_sequences` help control the quality and format of the generated response.

---

## 4. Setting Up Amazon S3 for Code Storage

To store the generated code, I created an Amazon **S3 bucket** with a structured folder (e.g., `code-output`) to organize output files. The Lambda function automatically saves each code snippet in this bucket, using a timestamped filename for uniqueness.

**Screenshot of the Empty S3 bucket**:
  
![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/2.%20S3%20Bucket%20Created.png>)

---

## 5. Setting Up API Gateway for External Access

I configured **API Gateway** to allow external access to the Lambda function, enabling users to submit requests via HTTP POST. The configuration includes:

1. **Integration with Lambda**:  
   API Gateway routes incoming requests to the Lambda function, passing along the JSON payload with user instructions.

2. **Defining Routes**:  
   I created a POST route (`/code-generation`) in API Gateway, with integration set to invoke the Lambda function.

**Screenshots of API Gateway integration and route configuration**:
    
![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/3.%20API%20Gateway%20Integration%20with%20Lambda%20Function.png>)
![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/4.%20API%20Gateway%20POST%20Route.png>)

---

## 6. Testing the API with Postman

I tested the API by sending a POST request via **Postman** to verify its functionality. The request included a JSON payload specifying the programming language and instructions for generating a binary search implementation in Python.

1. **Postman Request**:  
   I configured the POST request to send JSON data:
   ```json
   {
     "key": "python",
     "message": "implement binary search"
   }
   ```

2. **API Response**:  
   The response confirmed successful execution, showing that the code generation and storage processes worked as expected.

**Screenshot of the Postman request and response confirming successful execution**:
   
![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/5.%20API%20Calling%20Using%20POSTMAN.png>)

---

## 7. Verifying Output in S3 Bucket

After the Lambda function completed execution, I checked the S3 bucket to confirm that the generated code was saved correctly. The file `implement_binary_search.py` appeared in the `code-output` folder, verifying that the system performed end-to-end as intended.

**Screenshot of the generated code file stored in S3**:  

![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/6.%20S3%20Output%20file.png>)

---

## 8. Viewing the Generated Code in S3

Here is the content of the generated Python code for binary search. This snippet was generated based on the prompt provided and saved in the S3 bucket:

**Screenshot of the generated code file content**:  

![Alt text](<https://github.com/RhythmAhir/AWS_Bedrock_Code_Generation_Project/blob/main/Screenshots/7.%20Output%20Code.jpg>)

---

## Conclusion

This project successfully demonstrates my ability to integrate **AWS Lambda**, Bedrock's **"Anthropic Claude-v2"** model, **API Gateway**, and **Amazon S3** to build a serverless, code-generating API. The structured approach and configuration ensure that code can be generated based on natural language instructions, saved securely, and accessed via a public-facing API.

This solution is a scalable foundation for similar projects requiring automated text or code generation, making it a versatile tool for developers, educators, and businesses.
