def replaceElements(arr):
    n = len(arr)
    max_right = -1
    
    for i in range(n - 1, -1, -1):
        current = arr[i]
        arr[i] = max_right
        max_right = max(max_right, current)
    
    return arr

# Example 1
arr1 = [17, 18, 5, 4, 6, 1]
print(replaceElements(arr1)) 

# Example 2
arr2 = [400]
print(replaceElements(arr2))  
