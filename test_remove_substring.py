from solution_remove_substring import minLength, minLengthSimple


def test_example_1():
    """Test the example from the problem"""
    s = "ABFCACDB"
    # Let's trace:
    # "ABFCACDB" -> remove "AB" -> "FCACDB"
    # "FCACDB" -> remove "CD" -> "FCAB"
    # "FCAB" -> remove "AB" -> "FC"
    # Result: length = 2
    result = minLength(s)
    print(f"Test Example 1: s = 'ABFCACDB', minLength = {result}, expected = 2")
    assert result == 2
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 2")
    assert result_simple == 2
    print("PASSED: Test Example 1\n")


def test_example_2():
    """Test: s = 'ACBBD'"""
    s = "ACBBD"
    # "ACBBD" -> remove "CD" (from 'CB' not 'CD', so no removal initially)
    # Actually, there's no "AB" or "CD" in "ACBBD"
    # Final: length = 5
    result = minLength(s)
    print(f"Test Example 2: s = 'ACBBD', minLength = {result}, expected = 5")
    assert result == 5
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 5")
    assert result_simple == 5
    print("PASSED: Test Example 2\n")


def test_all_AB():
    """Test: s = 'ABAB'"""
    s = "ABAB"
    # "ABAB" -> remove "AB" -> "AB" -> remove "AB" -> ""
    result = minLength(s)
    print(f"Test All AB: s = 'ABAB', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test All AB\n")


def test_all_CD():
    """Test: s = 'CDCD'"""
    s = "CDCD"
    # "CDCD" -> remove "CD" -> "CD" -> remove "CD" -> ""
    result = minLength(s)
    print(f"Test All CD: s = 'CDCD', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test All CD\n")


def test_mixed():
    """Test: s = 'ABCD'"""
    s = "ABCD"
    # "ABCD" -> remove "AB" -> "CD" -> remove "CD" -> ""
    result = minLength(s)
    print(f"Test Mixed: s = 'ABCD', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test Mixed\n")


def test_cascading_removal():
    """Test cascading removals"""
    s = "ABABCD"
    # "ABABCD" -> remove "AB" -> "ABCD" -> remove "AB" -> "CD" -> remove "CD" -> ""
    result = minLength(s)
    print(f"Test Cascading: s = 'ABABCD', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test Cascading\n")


def test_cascading_removal_complex():
    """Test more complex cascading removals"""
    s = "ABCDCD"
    # "ABCDCD" -> remove "CD" -> "ABCD" -> remove "AB" -> "CD" -> remove "CD" -> ""
    result = minLength(s)
    print(f"Test Complex Cascading: s = 'ABCDCD', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test Complex Cascading\n")


def test_no_patterns():
    """Test string with no patterns"""
    s = "EFGHI"
    result = minLength(s)
    print(f"Test No Patterns: s = 'EFGHI', minLength = {result}, expected = 5")
    assert result == 5
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 5")
    assert result_simple == 5
    print("PASSED: Test No Patterns\n")


def test_empty_string():
    """Test empty string"""
    s = ""
    result = minLength(s)
    print(f"Test Empty: s = '', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test Empty\n")


def test_single_char():
    """Test single character"""
    s = "A"
    result = minLength(s)
    print(f"Test Single Char: s = 'A', minLength = {result}, expected = 1")
    assert result == 1
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 1")
    assert result_simple == 1
    print("PASSED: Test Single Char\n")


def test_nested_patterns():
    """Test nested pattern removals"""
    s = "ABCCD"
    # "ABCCD" -> remove "CD" -> "ABC" -> remove "AB" -> "C"
    result = minLength(s)
    print(f"Test Nested: s = 'ABCCD', minLength = {result}, expected = 1")
    assert result == 1
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 1")
    assert result_simple == 1
    print("PASSED: Test Nested\n")


def test_AB_CD_alternating():
    """Test alternating AB and CD"""
    s = "ABCDAB"
    # "ABCDAB" -> remove "AB" -> "CDAB" -> remove "CD" -> "AB" -> remove "AB" -> ""
    result = minLength(s)
    print(f"Test Alternating: s = 'ABCDAB', minLength = {result}, expected = 0")
    assert result == 0
    
    result_simple = minLengthSimple(s)
    print(f"Simple approach: minLength = {result_simple}, expected = 0")
    assert result_simple == 0
    print("PASSED: Test Alternating\n")


def run_all_tests():
    print("="*60)
    print("Running Remove Substring Tests")
    print("="*60 + "\n")
    
    test_example_1()
    test_example_2()
    test_all_AB()
    test_all_CD()
    test_mixed()
    test_cascading_removal()
    test_cascading_removal_complex()
    test_no_patterns()
    test_empty_string()
    test_single_char()
    test_nested_patterns()
    test_AB_CD_alternating()
    
    print("="*60)
    print("All tests passed!")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()