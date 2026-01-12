# Problem 0: A. Short Sort

## Problem Statement
**Title:** A. Short Sort  
**Difficulty:** Easy  
**Question ID:** 1873_A

### Problem Description
There are three cards with letters `a`, `b`, `c` placed in a row in some order. You can do the following operation at most once:
- Pick two cards, and swap them.

Is it possible that the row becomes `abc` after the operation? Output "YES" if it is possible, and "NO" otherwise.

### Input Format
- First line: integer `t` (1 ≤ t ≤ 6) — number of test cases
- For each test case: a single string of 3 characters (each of 'a', 'b', 'c' exactly once)

### Output Format
For each test case, output "YES" or "NO"

### Sample Input
```
6
abc
acb
bac
bca
cab
cba
```

### Sample Output
```
YES
YES
YES
NO
NO
YES
```

## Solution Approach

The key insight: We need to check if we can make the string "abc" with at most one swap.

1. If the string is already "abc", return "YES"
2. Try all possible single swaps (there are only 3C2 = 3 possible swaps):
   - Swap positions 0 and 1
   - Swap positions 0 and 2
   - Swap positions 1 and 2
3. For each swap, check if we get "abc"
4. If any swap results in "abc", return "YES"
5. Otherwise return "NO"

## How to Solve This Step-by-Step

1. Read the number of test cases `t`
2. For each test case:
   - Read a string `s` of length 3
   - Check if `s == "abc"` → YES
   - Check if swapping any two positions gives "abc" → YES
   - Otherwise → NO

## Expected Output for Sample
- Test 1: "abc" is already correct → YES
- Test 2: "acb" → swap positions 1,2 → "abc" → YES
- Test 3: "bac" → swap positions 0,1 → "abc" → YES
- Test 4: "bca" → no single swap makes "abc" → NO
- Test 5: "cab" → no single swap makes "abc" → NO
- Test 6: "cba" → swap positions 0,2 → "abc" → YES
