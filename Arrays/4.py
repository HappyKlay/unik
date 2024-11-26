def duplicateZeros(arr):
    zeros_count = arr.count(0)
    
    n = len(arr)
    
    i = n - 1 
    j = n + zeros_count - 1  
    
    while i >= 0:
        if arr[i] == 0:
            if j < n:
                arr[j] = 0
            j -= 1
            if j < n:
                arr[j] = 0
            j -= 1
        else:
            if j < n:
                arr[j] = arr[i]
            j -= 1
        i -= 1

    return arr

# Example 1
print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])) 

# Example 2
print(duplicateZeros([1, 2, 3])) 
