import sys
sys.path.insert(0, 'LiveCodeBench/solutions')
from solution_31 import solve
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
test_case("51230100", "512301")
test_case("1000", "1")
test_case("123", "123")
test_case("0", "0")
test_case("10", "1")