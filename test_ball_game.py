import sys
sys.path.insert(0, '.')
from solution_ball_game import find_losers

# Test from problem statement
n = 5
k = 2
result = find_losers(n, k)
print(f"Input: n = {n}, k = {k}")
print(f"Result (losers): {result}")
print()

# Test other cases
test_cases = [
    (5, 1),    # Simple case
    (3, 1),    # Small case
    (4, 2),    # n = 4, k = 2
    (6, 2),    # n = 6, k = 2
]

for n, k in test_cases:
    result = find_losers(n, k)
    print(f"Input: n = {n}, k = {k}")
    print(f"Result (losers): {result}")
    print()