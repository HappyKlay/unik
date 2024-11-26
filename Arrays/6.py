def removeDuplicates(nums):
    if not nums:
        return 0
    
    k = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1  
            nums[k] = nums[i]  
    
    return k + 1

# Example 1
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(k1, nums1[:k1]) 

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(k2, nums2[:k2]) 
