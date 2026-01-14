from collections import defaultdict

def longestEqualSubarray(nums, k):
    n = len(nums)
    freq = defaultdict(int)
    left = 0
    result = 0
    max_freq = 0
    
    for right in range(n):
        freq[nums[right]] += 1
        max_freq = max(max_freq, freq[nums[right]])
        
        # If we need to delete more than k elements, shrink window
        while (right - left + 1) - max_freq > k:
            freq[nums[left]] -= 1
            left += 1
            # Note: max_freq might become outdated, but that's okay
            # It just means our window might be smaller than optimal temporarily
            # This doesn't affect correctness
        
        # Update result with the count of most frequent element in current window
        result = max(result, max_freq)
    
    return result