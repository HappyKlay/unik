from collections import deque
from typing import List

def maxSubsequenceSum(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]
    
    dq = deque([0])

    for i in range(1, n):
        if dq[0] < i - k:
            dq.popleft()
        
        dp[i] = nums[i] + (dp[dq[0]] if dq else 0)
        
        max_sum = max(max_sum, dp[i])
        
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        
        dq.append(i)
    
    return max_sum

nums1 = [10, 2, -10, 5, 20]
k1 = 2
print(maxSubsequenceSum(nums1, k1))  # Output: 37

nums2 = [-1, -2, -3]
k2 = 1
print(maxSubsequenceSum(nums2, k2))  # Output: -1

nums3 = [10, -2, -10, -5, 20]
k3 = 2
print(maxSubsequenceSum(nums3, k3))  # Output: 23
