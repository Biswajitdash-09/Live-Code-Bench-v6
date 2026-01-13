from LiveCodeBench.solutions.solution_15 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
num1 = "1"
num2 = "12"
min_sum = 1
max_sum = 8
result = solution.countMethod(num1, num2, min_sum, max_sum)
print(f"Test 1: num1={num1}, num2={num2}, min_sum={min_sum}, max_sum={max_sum}")
print(f"Result: {result}")
print()

# Additional test cases
num1 = "1"
num2 = "5"
min_sum = 1
max_sum = 5
result2 = solution.countMethod(num1, num2, min_sum, max_sum)
print(f"Test 2: num1={num1}, num2={num2}, min_sum={min_sum}, max_sum={max_sum}")
print(f"Result: {result2}")
print(f"Expected: 5")
print()

num1 = "1"
num2 = "100"
min_sum = 1
max_sum = 1
result3 = solution.countMethod(num1, num2, min_sum, max_sum)
print(f"Test 3: num1={num1}, num2={num2}, min_sum={min_sum}, max_sum={max_sum}")
print(f"Result: {result3}")
print(f"Expected: Count numbers with digit sum = 1")
print()

num1 = "10"
num2 = "20"
min_sum = 1
max_sum = 10
result4 = solution.countMethod(num1, num2, min_sum, max_sum)
print(f"Test 4: num1={num1}, num2={num2}, min_sum={min_sum}, max_sum={max_sum}")
print(f"Result: {result4}")
print()

num1 = "1"
num2 = "1"
min_sum = 1
max_sum = 1
result5 = solution.countMethod(num1, num2, min_sum, max_sum)
print(f"Test 5: num1={num1}, num2={num2}, min_sum={min_sum}, max_sum={max_sum}")
print(f"Result: {result5}")
print(f"Expected: 1")
print()