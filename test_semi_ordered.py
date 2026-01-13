import sys
sys.path.insert(0, '.')
from solution_semi_ordered import min_operations_to_semi_ordered

# Test from problem statement
nums = [2, 1, 4, 3]
result = min_operations_to_semi_ordered(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 2")
print(f"Match: {result == 2}")
print()

# Test 2: Already semi-ordered
nums = [1, 2, 3, 4]
result = min_operations_to_semi_ordered(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 0 (already semi-ordered)")
print(f"Match: {result == 0}")
print()

# Test 3: Worst case - reversed
nums = [4, 3, 2, 1]
result = min_operations_to_semi_ordered(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
# 1 at index 3, n=4 at index 0
# swaps = 3 + (3 - 0) = 6, but pos_n < pos_1 so swaps = 5
print(f"Expected: 5")
print(f"Match: {result == 5}")
print()

# Test 4: Simple case
nums = [1, 3, 2]
result = min_operations_to_semi_ordered(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
# 1 at index 0, n=3 at index 1
# swaps = 0 + (2 - 1) = 1
print(f"Expected: 1")
print(f"Match: {result == 1}")
print()

# Test 5: Single element
nums = [1]
result = min_operations_to_semi_ordered(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 0 (already semi-ordered)")
print(f"Match: {result == 0}")
print()