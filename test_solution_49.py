from LiveCodeBench.solutions.solution_49 import maximumJumps

def test_example1():
    """
    Example 1:
    Input: nums = [1,3,6,4,1,2], target = 2
    Output: 3
    Explanation: Jump path: 0 -> 1 -> 3 -> 5
    """
    assert maximumJumps([1,3,6,4,1,2], 2) == 3

def test_example2():
    """
    Example 2:
    Input: nums = [1,3,6,4,1,2], target = 3
    Output: 5
    """
    assert maximumJumps([1,3,6,4,1,2], 3) == 5

def test_example3():
    """
    Example 3:
    Input: nums = [1,3,6,4,1,2], target = 0
    Output: -1 (no valid path)
    """
    assert maximumJumps([1,3,6,4,1,2], 0) == -1

if __name__ == "__main__":
    test_example1()
    print("Test 1 passed!")
    test_example2()
    print("Test 2 passed!")
    test_example3()
    print("Test 3 passed!")
    print("All tests passed!")