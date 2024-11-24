def validMountainArray(arr):
    n = len(arr)
    if n < 3:
        return False
    i = 0
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    if i == 0 or i == n - 1:
        return False
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1

# Example 1
arr1 = [2, 1]
print(validMountainArray(arr1)) 
# Example 2
arr2 = [3, 5, 5]
print(validMountainArray(arr2))  

# Example 3
arr3 = [0, 3, 2, 1]
print(validMountainArray(arr3)) 
