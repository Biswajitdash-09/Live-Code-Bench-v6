from solution import countZeroRequestServers

# Test case from the example
n = 3
logs = [[1,3],[2,6],[1,5]]
x = 5
queries = [10,11]
expected = [1, 2]

result = countZeroRequestServers(n, logs, x, queries)
print(f"Test 1 - Example case:")
print(f"Input: n={n}, logs={logs}, x={x}, queries={queries}")
print(f"Expected: {expected}")
print(f"Got: {result}")
print(f"Pass: {result == expected}\n")

# Additional test case: no logs at all
n = 3
logs = []
x = 5
queries = [10, 11]
expected = [3, 3]

result = countZeroRequestServers(n, logs, x, queries)
print(f"Test 2 - No logs:")
print(f"Input: n={n}, logs={logs}, x={x}, queries={queries}")
print(f"Expected: {expected}")
print(f"Got: {result}")
print(f"Pass: {result == expected}\n")

# Test case: all servers active
n = 2
logs = [[0,1],[0,2],[1,3]]
x = 5
queries = [3]
expected = [0]

result = countZeroRequestServers(n, logs, x, queries)
print(f"Test 3 - All servers active:")
print(f"Input: n={n}, logs={logs}, x={x}, queries={queries}")
print(f"Expected: {expected}")
print(f"Got: {result}")
print(f"Pass: {result == expected}\n")

# Test case: single server, single log
n = 1
logs = [[0,5]]
x = 1
queries = [5]
expected = [0]

result = countZeroRequestServers(n, logs, x, queries)
print(f"Test 4 - Single server, single log:")
print(f"Input: n={n}, logs={logs}, x={x}, queries={queries}")
print(f"Expected: {expected}")
print(f"Got: {result}")
print(f"Pass: {result == expected}\n")

# Test case: boundary conditions
n = 3
logs = [[0,0],[1,10],[2,20]]
x = 5
queries = [5]
expected = [2]

result = countZeroRequestServers(n, logs, x, queries)
print(f"Test 5 - Boundary conditions:")
print(f"Input: n={n}, logs={logs}, x={x}, queries={queries}")
print(f"Expected: {expected}")
print(f"Got: {result}")
print(f"Pass: {result == expected}\n")

print("All tests completed!")