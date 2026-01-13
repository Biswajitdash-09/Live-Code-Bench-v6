from solution_xor_derived import doesValidArrayExist, doesValidArrayExistOptimized, doesValidArrayExistMain


def test_example_1():
    """Test the example from the problem: derived = [1,1,0]"""
    derived = [1, 1, 0]
    # Let's verify manually:
    # If original = [0, 1, 0]:
    #   derived[0] = 0 ^ 1 = 1 ✓
    #   derived[1] = 1 ^ 0 = 1 ✓
    #   derived[2] = 0 ^ 0 = 0 ✓
    # So it should return True
    result = doesValidArrayExist(derived)
    print(f"Test Example 1: derived = [1,1,0], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    
    result_main = doesValidArrayExistMain(derived)
    print(f"Main function: {result_main}, expected = True")
    assert result_main == True
    print("PASSED: Test Example 1\n")


def test_example_2():
    """Test: derived = [1,0]"""
    derived = [1, 0]
    # XOR of all values = 1 ^ 0 = 1 ≠ 0, so should return False
    result = doesValidArrayExist(derived)
    print(f"Test Example 2: derived = [1,0], result = {result}, expected = False")
    assert result == False
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = False")
    assert result_opt == False
    
    result_main = doesValidArrayExistMain(derived)
    print(f"Main function: {result_main}, expected = False")
    assert result_main == False
    print("PASSED: Test Example 2\n")


def test_example_3():
    """Test: derived = [1,1]"""
    derived = [1, 1]
    # XOR of all values = 1 ^ 1 = 0, so should return True
    # Verify: original = [0, 1]
    #   derived[0] = 0 ^ 1 = 1 ✓
    #   derived[1] = 1 ^ 0 = 1 ✓
    result = doesValidArrayExist(derived)
    print(f"Test Example 3: derived = [1,1], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    
    result_main = doesValidArrayExistMain(derived)
    print(f"Main function: {result_main}, expected = True")
    assert result_main == True
    print("PASSED: Test Example 3\n")


def test_single_element():
    """Test: derived = [0] (single element)"""
    derived = [0]
    # For single element: derived[0] = original[0] ^ original[0] = 0
    result = doesValidArrayExist(derived)
    print(f"Test Single Element 0: derived = [0], result = {result}, expected = True")
    assert result == True
    
    derived = [1]
    # derived[0] = original[0] ^ original[0] = 0, but we have 1, so should return False
    result = doesValidArrayExist(derived)
    print(f"Test Single Element 1: derived = [1], result = {result}, expected = False")
    assert result == False
    print("PASSED: Test Single Element\n")


def test_all_zeros():
    """Test: derived = [0,0,0,0]"""
    derived = [0, 0, 0, 0]
    # XOR = 0, should return True
    # original = [0,0,0,0] works
    result = doesValidArrayExist(derived)
    print(f"Test All Zeros: derived = [0,0,0,0], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    print("PASSED: Test All Zeros passed\n")


def test_all_ones_even():
    """Test: derived = [1,1,1,1] (even length)"""
    derived = [1, 1, 1, 1]
    # XOR = 1 ^ 1 ^ 1 ^ 1 = 0, should return True
    result = doesValidArrayExist(derived)
    print(f"Test All Ones (4 elements): derived = [1,1,1,1], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    print("PASSED: Test All Ones (even)\n")


def test_all_ones_odd():
    """Test: derived = [1,1,1] (odd length)"""
    derived = [1, 1, 1]
    # XOR = 1 ^ 1 ^ 1 = 1 ≠ 0, should return False
    result = doesValidArrayExist(derived)
    print(f"Test All Ones (3 elements): derived = [1,1,1], result = {result}, expected = False")
    assert result == False
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = False")
    assert result_opt == False
    print("PASSED: Test All Ones (odd)\n")


def test_mixed_valid():
    """Test: derived = [1,0,1,0]"""
    derived = [1, 0, 1, 0]
    # XOR = 1 ^ 0 ^ 1 ^ 0 = 0, should return True
    result = doesValidArrayExist(derived)
    print(f"Test Mixed Valid: derived = [1,0,1,0], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    print("PASSED: Test Mixed Valid\n")


def test_mixed_invalid():
    """Test: derived = [1,0,1]"""
    derived = [1, 0, 1]
    # XOR = 1 ^ 0 ^ 1 = 0, should return True
    result = doesValidArrayExist(derived)
    print(f"Test Mixed Valid: derived = [1,0,1], result = {result}, expected = True")
    assert result == True
    
    result_opt = doesValidArrayExistOptimized(derived)
    print(f"Optimized version: {result_opt}, expected = True")
    assert result_opt == True
    print("PASSED: Test Mixed Valid\n")


def run_all_tests():
    print("="*60)
    print("Running XOR Derived Array Tests")
    print("="*60 + "\n")
    
    test_example_1()
    test_example_2()
    test_example_3()
    test_single_element()
    test_all_zeros()
    test_all_ones_even()
    test_all_ones_odd()
    test_mixed_valid()
    test_mixed_invalid()
    
    print("="*60)
    print("All tests passed!")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()