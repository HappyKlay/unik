from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    result = []

    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print(maxSlidingWindow(nums1, k1))  # Output: [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
print(maxSlidingWindow(nums2, k2))  # Output: [1]
