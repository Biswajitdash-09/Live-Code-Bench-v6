from solution_punishment_number import punishmentNumber, punishmentNumberOptimized


def test_example_1():
    """Test with n = 10"""
    n = 10
    # Verify which numbers from 1-10 are punishment numbers:
    # i=1: 1²=1, partition [1]=1 ✓ → add 1
    # i=2: 2²=4, partitions: [4]=4≠2 ✗
    # i=3: 3²=9, partitions: [9]=9≠3 ✗
    # i=4: 4²=16, partitions: [1,6]=7≠4, [16]=16≠4 ✗
    # i=5: 5²=25, partitions: [2,5]=7≠5, [25]=25≠5 ✗
    # i=6: 6²=36, partitions: [3,6]=9≠6, [36]=36≠6 ✗
    # i=7: 7²=49, partitions: [4,9]=13≠7, [49]=49≠7 ✗
    # i=8: 8²=64, partitions: [6,4]=10≠8, [64]=64≠8 ✗
    # i=9: 9²=81, partitions: [8,1]=9 ✓ → add 81
    # i=10: 10²=100, partitions: [10,0]=10 ✓ → add 100
    # Total: 1 + 81 + 100 = 182
    
    result = punishmentNumber(n)
    print(f"Test n=10: punishmentNumber({n}) = {result}, expected = 182")
    assert result == 182
    
    result_opt = punishmentNumberOptimized(n)
    print(f"Optimized: punishmentNumber({n}) = {result_opt}, expected = 182")
    assert result_opt == 182
    print("PASSED: Test n=10\n")


def test_small_values():
    """Test small values individually"""
    # Test n=1: only 1 is a punishment number → 1²=1
    result = punishmentNumber(1)
    print(f"Test n=1: punishmentNumber(1) = {result}, expected = 1")
    assert result == 1
    
    # Test n=2: still only 1 is punishment number → 1
    result = punishmentNumber(2)
    print(f"Test n=2: punishmentNumber(2) = {result}, expected = 1")
    assert result == 1
    
    # Test n=9: 1 and 9 are punishment numbers → 1² + 9² = 1 + 81 = 82
    result = punishmentNumber(9)
    print(f"Test n=9: punishmentNumber(9) = {result}, expected = 82")
    assert result == 82
    
    print("PASSED: Test Small Values\n")


def test_medium_values():
    """Test medium values"""
    # Test n=36
    # We know 1, 9, 10, and 36 are punishment numbers
    # 1²=1, 9²=81, 10²=100, 36²=1296
    # Total: 1 + 81 + 100 + 1296 = 1478
    
    result = punishmentNumber(36)
    print(f"Test n=36: punishmentNumber(36) = {result}, expected = 1478")
    assert result == 1478
    
    result_opt = punishmentNumberOptimized(36)
    print(f"Optimized: punishmentNumber(36) = {result_opt}, expected = 1478")
    assert result_opt == 1478
    print("PASSED: Test n=36\n")


def test_larger_values():
    """Test larger values"""
    # Test n=100
    result = punishmentNumber(100)
    print(f"Test n=100: punishmentNumber(100) = {result}")
    print("(Checking consistency with optimized version)")
    
    result_opt = punishmentNumberOptimized(100)
    print(f"Optimized: punishmentNumber(100) = {result_opt}")
    assert result == result_opt
    print("PASSED: Test n=100\n")


def test_edge_cases():
    """Test edge cases"""
    # Test n=0 (though problem says positive integer, we test for robustness)
    result = punishmentNumber(0)
    print(f"Test n=0: punishmentNumber(0) = {result}, expected = 0")
    assert result == 0


def test_known_punishment_numbers():
    """Test specific known punishment numbers"""
    # Known punishment numbers: 1, 9, 10, 36
    # Let's verify each individually
    
    known = [1, 9, 10, 36]
    for i in known:
        # Test if i is a punishment number
        # This is equivalent to checking if punishmentNumber(i) - punishmentNumber(i-1) == i²
        square = i * i
        prec = punishmentNumber(i-1) if i > 1 else 0
        curr = punishmentNumber(i)
        diff = curr - prec
        
        print(f"Test i={i}: square={square}, diff={diff}")
        assert diff == square, f"{i} should be a punishment number"
    
    print("PASSED: Test Known Punishment Numbers\n")


def run_all_tests():
    print("="*60)
    print("Running Punishment Number Tests")
    print("="*60 + "\n")
    
    test_example_1()
    test_small_values()
    test_medium_values()
    test_larger_values()
    test_edge_cases()
    test_known_punishment_numbers()
    
    print("="*60)
    print("All tests passed!")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()