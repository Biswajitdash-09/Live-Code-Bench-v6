def specialPerm(nums):
    n = len(nums)
    MOD = 10**9 + 7
    memo = {}
    
    def backtrack(remaining, last):
        if not remaining:
            return 1
        
        key = (tuple(remaining), last)
        if key in memo:
            return memo[key]
        
        count = 0
        for i, num in enumerate(remaining):
            if last % num == 0 or num % last == 0:
                new_remaining = remaining[:i] + remaining[i+1:]
                count += backtrack(new_remaining, num)
                count %= MOD
        
        memo[key] = count
        return count
    
    total = 0
    for i in range(n):
        new_remaining = nums[:i] + nums[i+1:]
        total += backtrack(new_remaining, nums[i])
        total %= MOD
    
    return total