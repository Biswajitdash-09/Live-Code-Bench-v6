from LiveCodeBench.solutions.solution_11 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
nums1 = [12, 9]
k1 = 1
result1 = solution.maximumOr(nums1, k1)
print(f"Test 1: nums = {nums1}, k = {k1}")
print(f"Result: {result1}")
print(f"Expected: 26 (doubling 9 gives 12 | 18 = 26)")
print()

# Additional test cases
nums2 = [1, 2, 3]
k2 = 2
result2 = solution.maximumOr(nums2, k2)
print(f"Test 2: nums = {nums2}, k = {k2}")
print(f"Result: {result2}")
print()

nums3 = [1]
k3 = 5
result3 = solution.maximumOr(nums3, k3)
print(f"Test 3: nums = {nums3}, k = {k3}")
print(f"Result: {result3}")
print(f"Expected: 32 (1 * 2^5 = 32)")
print()

nums4 = [7, 8, 15]
k4 = 1
result4 = solution.maximumOr(nums4, k4)
print(f"Test 4: nums = {nums4}, k = {k4}")
print(f"Result: {result4}")
print()