from LiveCodeBench.solutions.solution_16 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
nums1 = [1,2,3,4,5]
result1 = solution.distinctDifferenceArray(nums1)
print(f"Test 1: nums = {nums1}")
print(f"Result: {result1}")
print()

# Additional test cases
nums2 = [3,2,3,4,2]
result2 = solution.distinctDifferenceArray(nums2)
print(f"Test 2: nums = {nums2}")
print(f"Result: {result2}")
print()

nums3 = [1,1,1,1]
result3 = solution.distinctDifferenceArray(nums3)
print(f"Test 3: nums = {nums3}")
print(f"Result: {result3}")
print(f"Expected: All prefixes have 1 distinct, all suffixes (after last) have 0")
print()

nums4 = [1]
result4 = solution.distinctDifferenceArray(nums4)
print(f"Test 4: nums = {nums4}")
print(f"Result: {result4}")
print(f"Expected: [1] (prefix has 1, suffix empty has 0)")
print()

nums5 = [1,2,1,2]
result5 = solution.distinctDifferenceArray(nums5)
print(f"Test 5: nums = {nums5}")
print(f"Result: {result5}")
print()