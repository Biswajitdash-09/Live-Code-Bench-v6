from LiveCodeBench.solutions.solution_10 import sumInAMatrix

def test_solution():
    # Test case 1: Example from problem
    nums1 = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
    result1 = sumInAMatrix(nums1)
    print(f"Test 1: {result1} (expected: 15)")
    assert result1 == 15, f"Test 1 failed: expected 15, got {result1}"
    
    # Test case 2: Single element
    nums2 = [[5]]
    result2 = sumInAMatrix(nums2)
    print(f"Test 2: {result2} (expected: 5)")
    assert result2 == 5, f"Test 2 failed: expected 5, got {result2}"
    
    # Test case 3: Two rows, two columns
    nums3 = [[1,2],[3,4]]
    result3 = sumInAMatrix(nums3)
    print(f"Test 3: {result3} (expected: 7)")  # max(2,4) + max(1,3) = 4 + 3 = 7
    assert result3 == 7, f"Test 3 failed: expected 7, got {result3}"
    
    # Test case 4: All same values
    nums4 = [[3,3],[3,3]]
    result4 = sumInAMatrix(nums4)
    print(f"Test 4: {result4} (expected: 6)")  # 3 + 3 = 6
    assert result4 == 6, f"Test 4 failed: expected 6, got {result4}"
    
    # Test case 5: Single row with multiple elements
    nums5 = [[5,3,1]]
    result5 = sumInAMatrix(nums5)
    print(f"Test 5: {result5} (expected: 9)")  # 5 + 3 + 1 = 9
    assert result5 == 9, f"Test 5 failed: expected 9, got {result5}"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()