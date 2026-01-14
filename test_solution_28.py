from LiveCodeBench.solutions.solution_28 import find_the_maximum_achievable_number

def test_find_the_maximum_achievable_number():
    # Example 1: num = 4, t = 1
    # x = 5: start with (5, 4), after 1 operation: decrease x by 1, increase num by 1 -> (4, 5)
    # x = 4 equals the original num
    assert find_the_maximum_achievable_number(4, 1) == 5
    
    # Example 2: num = 2, t = 1
    # x = 3: start with (3, 2), after 1 operation: decrease x by 1, increase num by 1 -> (2, 3)
    # x = 2 equals the original num
    assert find_the_maximum_achievable_number(2, 1) == 3
    
    # Additional test cases
    # num = 3, t = 2
    # Maximum achievable is 5 (3 + 2)
    assert find_the_maximum_achievable_number(3, 2) == 5
    
    # num = 10, t = 0
    # No operations allowed, only achievable number is num itself
    assert find_the_maximum_achievable_number(10, 0) == 10
    
    # num = 1, t = 5
    # Maximum achievable is 6 (1 + 5)
    assert find_the_maximum_achievable_number(1, 5) == 6
    
    print("All tests passed!")

if __name__ == "__main__":
    test_find_the_maximum_achievable_number()