import sys
from typing import List

def longest_semi_repetitive_substring(s: str) -> int:
    """
    Find the length of the longest semi-repetitive substring.
    Semi-repetitive means at most one consecutive pair of the same digits.
    """
    if not s:
        return 0
    
    n = len(s)
    count = 0  # Count of consecutive pairs
    left = 0
    max_len = 1
    prev_pair_start = -1  # Start index of the previous consecutive pair
    
    for j in range(1, n):
        if s[j-1] == s[j]:
            count += 1
            prev_pair_start = j - 1
        
        # Shrink window if count > 1
        while count > 1:
            if s[left] == s[left+1]:
                count -= 1
            left += 1
        
        max_len = max(max_len, j - left + 1)
    
    return max_len

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    outputs = []
    for _ in range(t):
        s = data[idx]
        idx += 1
        
        result = longest_semi_repetitive_substring(s)
        outputs.append(str(result))
    
    print('\n'.join(outputs))

if __name__ == "__main__":
    main()