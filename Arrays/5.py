def merge(nums1, m, nums2, n):
    i = m - 1  
    j = n - 1 
    k = m + n - 1 
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    
    return nums1

# Example 1
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))

# Example 2
print(merge([1], 1, [], 0)) 

# Example 3
print(merge([0], 0, [1], 1)) 
