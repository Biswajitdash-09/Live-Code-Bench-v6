from LiveCodeBench.solutions.solution_37 import longestEqualSubarray

# Test cases
test_cases = [
    # Example 1 (incomplete in problem, but likely answer is 3)
    # nums = [1,3,2,3,1,3], k = 3
    # Can create [3,3,3] by deleting 1,2,1
    ([1,3,2,3,1,3], 3, 3),
    
    # Test case 2: All same elements, no deletions needed
    ([1,1,1,1], 2, 4),
    
    # Test case 3: Same elements but with deletions
    ([1,1,1,1], 0, 4),
    
    # Test case 4: Different elements, need deletions
    ([1,2,3,4], 2, 1),
    
    # Test case 5: Empty array
    ([], 5, 0),
    
    # Test case 6: Single element
    ([5], 0, 1),
    
    # Test case 7: Alternating elements
    ([1,2,1,2,1,2], 2, 3),
    
    # Test case 8: Large k value
    ([1,2,1,2,1], 10, 3),
    
    # Test case 9: No deletions allowed (k=0)
    ([1,1,2,2,3,3], 0, 2),
    
    # Test case 10: Complex case
    ([1,2,3,1,1,2,2,1], 2, 3),
]

print("Running tests for solution_37...")
passed = 0
failed = 0

for i, (nums, k, expected) in enumerate(test_cases):
    result = longestEqualSubarray(nums, k)
    if result == expected:
        print(f"Test {i+1}: PASSED - longestEqualSubarray({nums}, {k}) = {result}")
        passed += 1
    else:
        print(f"Test {i+1}: FAILED - longestEqualSubarray({nums}, {k}) = {result}, expected {expected}")
        failed += 1

print(f"\nResults: {passed} passed, {failed} failed")