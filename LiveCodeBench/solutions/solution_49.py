from typing import List

def maximumJumps(nums: List[int], target: int) -> int:
    """
    Return the maximum number of jumps to reach the last index.
    
    In one step, you can jump from index i to any index j such that
    0 <= i < j < n and -target <= nums[j] - nums[i] <= target.
    """
    n = len(nums)
    
    # dp[i] = maximum number of jumps to reach index i
    dp = [-float('inf')] * n
    dp[0] = 0  # Starting point with 0 jumps
    
    for i in range(n):
        # If we can reach index i
        if dp[i] != -float('inf'):
            # Try to jump from i to all indices j > i
            for j in range(i + 1, n):
                diff = nums[j] - nums[i]
                if -target <= diff <= target:
                    # Make a jump to j
                    if dp[j] < dp[i] + 1:
                        dp[j] = dp[i] + 1
    
    # Return -1 if we can't reach the last index
    if dp[n - 1] == -float('inf'):
        return -1
    return dp[n - 1]