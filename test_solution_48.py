from LiveCodeBench.solutions.solution_48 import minimizeStringLength

# Test cases
test_cases = [
    # Example 1 from problem
    (["aa","ab","bc"], 4),
    
    # Example 2 from problem
    (["ab","b"], 2),
    
    # Example 3 from problem
    (["aaa","c","aba"], 6),
    
    # Additional test case: ["ab","ba"]
    (["ab","ba"], 3),
    
    # Additional test case: ["a","b","c"]
    (["a","b","c"], 3),
    
    # Additional test case: ["ab","bc","ca"]
    (["ab","bc","ca"], 4),
]

print("Running tests for solution_48...")
passed = 0
failed = 0

for i, (words, expected) in enumerate(test_cases):
    result = minimizeStringLength(words)
    if result == expected:
        print(f"Test {i+1}: PASSED - minimizeStringLength({words}) = {result}")
        passed += 1
    else:
        print(f"Test {i+1}: FAILED - minimizeStringLength({words}) = {result}, expected {expected}")
        failed += 1

print(f"\nResults: {passed} passed, {failed} failed")