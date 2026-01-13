import sys
sys.path.insert(0, '.')
from solution_power_groups import solve_array

# Test from problem statement example
nums = [2, 1, 4]
result = solve_array(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 141")
print(f"Match: {result == 141}")
print()

# Test with empty array
nums = []
result = solve_array(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 0")
print(f"Match: {result == 0}")
print()

# Test with single element
nums = [5]
result = solve_array(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 125 (5^2 * 5)")
print(f"Match: {result == 125}")
print()

# Test with same elements
nums = [3, 3, 3]
result = solve_array(nums)
print(f"Input: {nums}")
print(f"Result: {result}")
print(f"Expected: 267 (7 subsets * 3^2*3 = 7*27 = 189, need to recalculate)")
print()

# Let's manually calculate for [3,3,3]:
# {3}: 3^2*3 = 27
# {3}: 27
# {3}: 27
# {3,3}: 3^2*3 = 27
# {3,3}: 27
# {3,3}: 27
# {3,3,3}: 3^2*3 = 27
# Total = 7 * 27 = 189
print(f"For [3,3,3]: 7 subsets, each 27, total = 189")
print()