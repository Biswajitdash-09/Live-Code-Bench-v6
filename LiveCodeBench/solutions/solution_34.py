from LiveCodeBench.solutions.solution_34 import canTraverseAllPairs

def test_example1():
    # Example from problem: nums = [2,3,6]
    # gcd(2,3) = 1, gcd(2,6) = 2, gcd(3,6) = 3
    # 0 connected to 2 (via 6), 1 connected to 2 (via 6), all connected
    result = canTraverseAllPairs([2, 3, 6])
    print(f"Test [2, 3, 6]: {result}")
    assert result == True, "Expected True for [2, 3, 6]"

def test_example2():
    # Example from problem
    # If all numbers are same
    result = canTraverseAllPairs([4, 4, 4])
    print(f"Test [4, 4, 4]: {result}")
    assert result == True, "Expected True for [4, 4, 4]"

def test_disconnected():
    # nums = [2, 3, 5]
    # All primes, no common factors
    result = canTraverseAllPairs([2, 3, 5])
    print(f"Test [2, 3, 5]: {result}")
    assert result == False, "Expected False for [2, 3, 5]"

def test_single_element():
    # Single element should always return True
    result = canTraverseAllPairs([5])
    print(f"Test [5]: {result}")
    assert result == True, "Expected True for single element"

def test_connected_via_primes():
    # nums = [6, 10, 15]
    # 6 = 2*3, 10 = 2*5, 15 = 3*5
    # 6 connected to 10 (via 2), 6 connected to 15 (via 3), 10 connected to 15 (via 5)
    result = canTraverseAllPairs([6, 10, 15])
    print(f"Test [6, 10, 15]: {result}")
    assert result == True, "Expected True for [6, 10, 15]"

def test_connected():
    # nums = [2, 4, 8, 16]
    # All powers of 2, should be connected
    result = canTraverseAllPairs([2, 4, 8, 16])
    print(f"Test [2, 4, 8, 16]: {result}")
    assert result == True, "Expected True for [2, 4, 8, 16]"

def test_disconnected_with_bridge():
    # nums = [2, 3, 10, 15]
    # 2-10 connected, 3-15 connected, 10-15 connected (via 5)
    # But 2 and 3 need a path
    # Let's trace: 2 (i=0) connects to 10 (i=2) via prime 2
    # 3 (i=1) connects to 15 (i=3) via prime 3
    # 10 (i=2) and 15 (i=3) connect via prime 5
    # So 0-2-3-1 forms a path, all connected!
    result = canTraverseAllPairs([2, 3, 10, 15])
    print(f"Test [2, 3, 10, 15]: {result}")
    assert result == True, "Expected True for [2, 3, 10, 15]"

if __name__ == "__main__":
    print("Running tests for solution_34 (greatest-common-divisor-traversal)...\n")
    
    test_example1()
    test_example2()
    test_disconnected()
    test_single_element()
    test_connected_via_primes()
    test_connected()
    test_disconnected_with_bridge()
    
    print("\nAll tests passed!")