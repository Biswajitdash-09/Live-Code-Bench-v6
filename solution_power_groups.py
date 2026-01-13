import sys
from typing import List

MOD = 10**9 + 7

def solve_array(nums: List[int]) -> int:
    """
    Calculate the sum of the power of all non-empty groups.
    Power = max(nums[i])^2 * min(nums[i])
    """
    if not nums:
        return 0
    
    result = 0
    n = len(nums)
    
    # Enumerate all non-empty subsets using bitmask
    # There are 2^n - 1 non-empty subsets
    for mask in range(1, 1 << n):
        max_val = float('-inf')
        min_val = float('inf')
        
        for i in range(n):
            if mask & (1 << i):
                max_val = max(max_val, nums[i])
                min_val = min(min_val, nums[i])
        
        # Calculate power: max^2 * min
        power = (max_val * max_val % MOD) * min_val % MOD
        result = (result + power) % MOD
    
    return result % MOD

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    t = int(data[idx])
    idx += 1
    
    outputs = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        
        result = solve_array(arr)
        outputs.append(str(result))
    
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()