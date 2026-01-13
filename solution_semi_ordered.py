import sys
from typing import List

def min_operations_to_semi_ordered(nums: List[int]) -> int:
    """
    Find the minimum number of adjacent swaps to make a permutation semi-ordered.
    Semi-ordered means first element is 1 and last element is n.
    """
    if not nums:
        return 0
    
    n = len(nums)
    
    # Find positions of 1 and n
    pos_1 = -1
    pos_n = -1
    
    for i in range(n):
        if nums[i] == 1:
            pos_1 = i
        elif nums[i] == n:
            pos_n = i
    
    # Calculate swap count
    # Swaps needed for 1: from pos_1 to position 0
    # Swaps needed for n: from pos_n to position n-1
    swaps = pos_1 + (n - 1 - pos_n)
    
    # If n is to the left of 1, moving 1 to position 0 will shift n right by 1
    if pos_n < pos_1:
        swaps -= 1
    
    return swaps

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    outputs = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        
        result = min_operations_to_semi_ordered(arr)
        outputs.append(str(result))
    
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()