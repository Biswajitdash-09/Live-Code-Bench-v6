from LiveCodeBench.solutions.solution_17 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
n1 = 4
queries1 = [[0,2],[1,2],[3,1],[1,1],[2,1]]
result1 = solution.colorTheArray(n1, queries1)
print(f"Test 1: n = {n1}, queries = {queries1}")
print(f"Result: {result1}")
print()

# Additional test cases
n2 = 3
queries2 = [[0,1],[1,1],[2,1]]
result2 = solution.colorTheArray(n2, queries2)
print(f"Test 2: n = {n2}, queries = {queries2}")
print(f"Result: {result2}")
print()

n3 = 5
queries3 = [[0,1],[4,1],[2,1]]
result3 = solution.colorTheArray(n3, queries3)
print(f"Test 3: n = {n3}, queries = {queries3}")
print(f"Result: {result3}")
print()

n4 = 2
queries4 = [[0,1],[1,1]]
result4 = solution.colorTheArray(n4, queries4)
print(f"Test 4: n = {n4}, queries = {queries4}")
print(f"Result: {result4}")
print()

n5 = 1
queries5 = [[0,1]]
result5 = solution.colorTheArray(n5, queries5)
print(f"Test 5: n = {n5}, queries = {queries5}")
print(f"Result: {result5}")
print()

n6 = 4
queries6 = [[0,1],[1,2],[2,3],[3,4]]
result6 = solution.colorTheArray(n6, queries6)
print(f"Test 6: n = {n6}, queries = {queries6}")
print(f"Result: {result6}")
print()