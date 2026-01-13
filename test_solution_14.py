from LiveCodeBench.solutions.solution_14 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
prices1 = [1,2,2]
money1 = 3
result1 = solution.buyChoco(prices1, money1)
print(f"Test 1: prices = {prices1}, money = {money1}")
print(f"Result: {result1}")
print()

# Additional test cases
prices2 = [3,2,3]
money2 = 3
result2 = solution.buyChoco(prices2, money2)
print(f"Test 2: prices = {prices2}, money = {money2}")
print(f"Result: {result2}")
print(f"Expected: 3 (can't afford two cheapest: 2+3=5 > 3)")
print()

prices3 = [1,1,1]
money3 = 7
result3 = solution.buyChoco(prices3, money3)
print(f"Test 3: prices = {prices3}, money = {money3}")
print(f"Result: {result3}")
print(f"Expected: 5 (1+1=2, leftover: 7-2=5)")
print()

prices4 = [5,5]
money4 = 10
result4 = solution.buyChoco(prices4, money4)
print(f"Test 4: prices = {prices4}, money = {money4}")
print(f"Result: {result4}")
print(f"Expected: 0 (5+5=10, leftover: 10-10=0)")
print()

prices5 = [5,5]
money5 = 11
result5 = solution.buyChoco(prices5, money5)
print(f"Test 5: prices = {prices5}, money = {money5}")
print(f"Result: {result5}")
print(f"Expected: 1 (5+5=10, leftover: 11-10=1)")
print()

prices6 = [10,20]
money6 = 5
result6 = solution.buyChoco(prices6, money6)
print(f"Test 6: prices = {prices6}, money = {money6}")
print(f"Result: {result6}")
print(f"Expected: 5 (can't afford two: 10+20=30 > 5)")
print()