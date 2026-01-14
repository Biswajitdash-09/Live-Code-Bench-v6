import sys
sys.path.insert(0, 'LiveCodeBench/solutions')
from solution_32 import solve
import io

def test_case(input_str, expected):
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    
    # Provide input
    sys.stdin = io.StringIO(input_str + '\n')
    solve()
    
    # Get output
    output = sys.stdout.getvalue().strip()
    
    # Restore stdout
    sys.stdout = old_stdout
    
    print(f"Input: '{input_str}' -> Output: '{output}' (Expected: '{expected}') - {'PASS' if output == expected else 'FAIL'}")
    return output == expected

# Test cases
# Example 1: 192 -> 192, 384, 576 -> 192384576 (contains all digits 1-9 exactly once)
test_case("192", "true")

# Example 2: 100 -> 100, 200, 300 -> 100200300 (contains 0s and duplicates)
test_case("100", "false")

# Additional test: 273 -> 273, 546, 819 -> 273546819 (contains all digits 1-9 exactly once)
test_case("273", "true")

# Additional test: 123 -> 123, 246, 369 -> 123246369 (contains duplicates and missing digits)
test_case("123", "false")

# Additional test: 999 -> 999, 1998, 2997 -> too many digits (more than 9)
test_case("999", "false")

# Additional test: 327 -> 327, 654, 981 -> 327654981 (contains all digits 1-9 exactly once)
test_case("327", "true")

# Additional test: 192 is the classic fascinating number
test_case("192", "true")

# Additional test: 999 creates numbers with more than 9 digits total
test_case("999", "false")

# Additional test: 819 -> 819, 1638, 2457 -> too many digits (more than 9)
test_case("819", "false")