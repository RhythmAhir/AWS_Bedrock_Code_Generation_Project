Here is Python code to implement binary search:

```python
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < x:
            low = mid + 1
            
        elif arr[mid] > x:
            high = mid - 1
            
        else:
            return mid
        
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14] 
x = 10

result = binary_search(arr, x)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found in array")
```

This implements a recursive binary search algorithm. It takes an sorted array `arr` and a value `x` to search for. It starts by comparing `x` to the middle element of `arr`. If `x` matches that element, it returns the index. If `x` is less than the middle, it recurses on the left half of `arr`. If `x` is greater, it recurses on the right half. It returns -1 if `x` is not found in `arr`.