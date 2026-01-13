from LiveCodeBench.solutions.solution_13 import Solution

# Test with provided example
solution = Solution()

# Example from the problem description
s1 = "leetscode"
dictionary1 = ["leet","code","leetcode"]
result1 = solution.minExtraChar(s1, dictionary1)
print(f"Test 1: s = \"{s1}\", dictionary = {dictionary1}")
print(f"Result: {result1}")
print()

# Additional test cases
s2 = "sayhelloworld"
dictionary2 = ["hello","world"]
result2 = solution.minExtraChar(s2, dictionary2)
print(f"Test 2: s = \"{s2}\", dictionary = {dictionary2}")
print(f"Result: {result2}")
print(f"Expected: 3 (\"say\" are the extra characters)")
print()

s3 = "leetcode"
dictionary3 = ["leet","code","leetcode"]
result3 = solution.minExtraChar(s3, dictionary3)
print(f"Test 3: s = \"{s3}\", dictionary = {dictionary3}")
print(f"Result: {result3}")
print(f"Expected: 0 (whole string matches)")
print()

s4 = "abc"
dictionary4 = ["a","b","c"]
result4 = solution.minExtraChar(s4, dictionary4)
print(f"Test 4: s = \"{s4}\", dictionary = {dictionary4}")
print(f"Result: {result4}")
print(f"Expected: 0")
print()

s5 = "xyz"
dictionary5 = ["ab","cd"]
result5 = solution.minExtraChar(s5, dictionary5)
print(f"Test 5: s = \"{s5}\", dictionary = {dictionary5}")
print(f"Result: {result5}")
print(f"Expected: 3 (no matches, all characters are extra)")
print()

s6 = "a"
dictionary6 = ["a"]
result6 = solution.minExtraChar(s6, dictionary6)
print(f"Test 6: s = \"{s6}\", dictionary = {dictionary6}")
print(f"Result: {result6}")
print(f"Expected: 0")
print()

s7 = "a"
dictionary7 = ["b"]
result7 = solution.minExtraChar(s7, dictionary7)
print(f"Test 7: s = \"{s7}\", dictionary = {dictionary7}")
print(f"Result: {result7}")
print(f"Expected: 1")
print()