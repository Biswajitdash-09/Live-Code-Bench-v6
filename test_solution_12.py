from LiveCodeBench.solutions.solution_12 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
nums1 = [3,-1,-5,2,5,-9]
result1 = solution.maxStrength(nums1)
print(f"Test 1: nums = {nums1}")
print(f"Result: {result1}")
print()

# Additional test cases
nums2 = [1, 2, 3]
result2 = solution.maxStrength(nums2)
print(f"Test 2: nums = {nums2}")
print(f"Result: {result2}")
print(f"Expected: 6 (product of all)")
print()

nums3 = [-1, -2, -3]
result3 = solution.maxStrength(nums3)
print(f"Test 3: nums = {nums3}")
print(f"Result: {result3}")
print(f"Expected: 6 (product of all)")
print()

nums4 = [-1]
result4 = solution.maxStrength(nums4)
print(f"Test 4: nums = {nums4}")
print(f"Result: {result4}")
print(f"Expected: -1")
print()

nums5 = [1]
result5 = solution.maxStrength(nums5)
print(f"Test 5: nums = {nums5}")
print(f"Result: {result5}")
print(f"Expected: 1")
print()

nums6 = [0, -1]
result6 = solution.maxStrength(nums6)
print(f"Test 6: nums = {nums6}")
print(f"Result: {result6}")
print()

nums7 = [3, -2, 1, 4]
result7 = solution.maxStrength(nums7)
print(f"Test 7: nums = {nums7}")
print(f"Result: {result7}")
print()