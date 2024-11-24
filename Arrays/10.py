def sortArrayByParity(nums):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        if nums[left] % 2 == 0: 
            left += 1
        elif nums[right] % 2 == 1: 
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums

# Example 1
nums1 = [3, 1, 2, 4]
print(sortArrayByParity(nums1)) 

# Example 2
nums2 = [0]
print(sortArrayByParity(nums2))  
