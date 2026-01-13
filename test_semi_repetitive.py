import sys
sys.path.insert(0, '.')
from solution_semi_repetitive import longest_semi_repetitive_substring

# Test from problem statement
s = "52233"
result = longest_semi_repetitive_substring(s)
print(f"Input: {s}")
print(f"Result: {result}")
print()

# Test other cases
test_cases = [
    ("0010", 4),
    ("002020", 6),
    ("0123", 4),
    ("2002", 4),
    ("54944", 5),
    ("00101022", 5),  # Should be less than length 8
    ("111", 2),  # Has "11" and "11" - but these overlap, so max 2
    ("1122", 3),  # "112" or "122" - only one consecutive pair
    ("1223", 3),
    ("12", 2),
]

for test_str, expected in test_cases:
    result = longest_semi_repetitive_substring(test_str)
    print(f"Input: {test_str}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    print(f"Match: {result == expected}")
    print()