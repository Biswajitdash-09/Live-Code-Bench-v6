import sys
sys.path.insert(0, '.')
from solution_power_groups import solve_array

# Test Case 1: Manual verification for [0, 1, 2]
nums = [0, 1, 2]
print(f"Testing array: {nums}")
result = solve_array(nums)
print(f"Result: {result}")

# Let's manually calculate:
# All subsets and their power (max^2 * min):
# {0}: 0^2*0 = 0
# {1}: 1^2*1 = 1
# {2}: 2^2*2 = 8
# {0,1}: max=1, min=0, power=1^2*0 = 0
# {0,2}: max=2, min=0, power=2^2*0 = 0
# {1,2}: max=2, min=1, power=2^2*1 = 4
# {0,1,2}: max=2, min=0, power=2^2*0 = 0
# Total = 0+1+8+0+0+4+0 = 13
print(f"Expected: 13 (0+1+8+0+0+4+0)")
print(f"Match: {result == 13}")
print()

# Test Case 2: Manual verification for [4, 3, 2, 3, 4]
nums = [4, 3, 2, 3, 4]
print(f"Testing array: {nums}")
result = solve_array(nums)
print(f"Result: {result}")
print(f"Expected: 1151 (from test output)")
print(f"Match: {result == 1151}")
print()

# Test Case 3: Manual verification for all 9s
nums = [9, 9, 9, 9, 9, 9, 9, 9, 9]
print(f"Testing array: {nums}")
result = solve_array(nums)
print(f"Result: {result}")

# 9^2*9 = 729
# There are 2^9 - 1 = 511 subsets
# Each subset contributes 729
# Total = 511 * 729 = 372,519
expected = (511 * 729) % (10**9 + 7)
print(f"Expected: {expected} (511 subsets * 729 each)")
print(f"Match: {result == expected}")