import sys
sys.path.insert(0, 'LiveCodeBench/solutions')
from solution_36 import Solution

def test_example1():
    """
    Example from problem: nums = [2,5,1,4]
    Pairs and analysis:
    - (0,1): first(2) and last(5), gcd(2,5)=1, beautiful
    - (0,2): first(2) and last(1), gcd(2,1)=1, beautiful
    - (0,3): first(2) and last(4), gcd(2,4)=2, not beautiful
    - (1,2): first(5) and last(1), gcd(5,1)=1, beautiful
    - (1,3): first(5) and last(4), gcd(5,4)=1, beautiful
    - (2,3): first(1) and last(4), gcd(1,4)=1, beautiful
    Total: 5 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([2, 5, 1, 4])
    print(f"Test [2, 5, 1, 4]: {result}")
    assert result == 5, f"Expected 5 for [2, 5, 1, 4], got {result}"

def test_single_element():
    """
    Single element - no pairs possible
    """
    sol = Solution()
    result = sol.countBeautifulPairs([5])
    print(f"Test [5]: {result}")
    assert result == 0, f"Expected 0 for single element, got {result}"

def test_all_coprime():
    """
    All pairs are coprime: nums = [1, 2, 3]
    - (0,1): first(1) and last(2), gcd(1,2)=1, beautiful
    - (0,2): first(1) and last(3), gcd(1,3)=1, beautiful
    - (1,2): first(2) and last(3), gcd(2,3)=1, beautiful
    Total: 3 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([1, 2, 3])
    print(f"Test [1, 2, 3]: {result}")
    assert result == 3, f"Expected 3 for [1, 2, 3], got {result}"

def test_none_coprime():
    """
    No pairs are coprime: nums = [2, 4, 6]
    First digits: 2, 4, 6
    Last digits: 2, 4, 6
    - (0,1): gcd(2,4)=2, not beautiful
    - (0,2): gcd(2,6)=2, not beautiful
    - (1,2): gcd(4,6)=2, not beautiful
    Total: 0 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([2, 4, 6])
    print(f"Test [2, 4, 6]: {result}")
    assert result == 0, f"Expected 0 for [2, 4, 6], got {result}"

def test_two_elements():
    """
    Two elements: nums = [11, 22]
    - (0,1): first(1) and last(2), gcd(1,2)=1, beautiful
    Total: 1 beautiful pair
    """
    sol = Solution()
    result = sol.countBeautifulPairs([11, 22])
    print(f"Test [11, 22]: {result}")
    assert result == 1, f"Expected 1 for [11, 22], got {result}"

def test_two_elements_not_coprime():
    """
    Two elements not coprime: nums = [12, 24]
    - (0,1): first(1) and last(4), gcd(1,4)=1, beautiful (wait, 1 is coprime with everything)
    Actually, 1 and 4 are coprime
    Total: 1 beautiful pair
    """
    sol = Solution()
    result = sol.countBeautifulPairs([12, 24])
    print(f"Test [12, 24]: {result}")
    assert result == 1, f"Expected 1 for [12, 24], got {result}"

def test_multi_digit_numbers():
    """
    Multi-digit numbers: nums = [123, 456, 789]
    - (0,1): first(1) and last(6), gcd(1,6)=1, beautiful
    - (0,2): first(1) and last(9), gcd(1,9)=1, beautiful
    - (1,2): first(4) and last(9), gcd(4,9)=1, beautiful
    Total: 3 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([123, 456, 789])
    print(f"Test [123, 456, 789]: {result}")
    assert result == 3, f"Expected 3 for [123, 456, 789], got {result}"

def test_mixed_pairs():
    """
    Mixed pairs: nums = [21, 31, 21]
    First digits: 2, 3, 2
    Last digits: 1, 1, 1
    - (0,1): first(2) and last(1), gcd(2,1)=1, beautiful
    - (0,2): first(2) and last(1), gcd(2,1)=1, beautiful
    - (1,2): first(3) and last(1), gcd(3,1)=1, beautiful
    Total: 3 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([21, 31, 21])
    print(f"Test [21, 31, 21]: {result}")
    assert result == 3, f"Expected 3 for [21, 31, 21], got {result}"

def test_all_same_first_digit():
    """
    All same first digit: nums = [11, 12, 13]
    First digits: 1, 1, 1 (all 1, coprime with everything)
    - (0,1): gcd(1,2)=1, beautiful
    - (0,2): gcd(1,3)=1, beautiful
    - (1,2): gcd(1,3)=1, beautiful
    Total: 3 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([11, 12, 13])
    print(f"Test [11, 12, 13]: {result}")
    assert result == 3, f"Expected 3 for [11, 12, 13], got {result}"

def test_all_same_last_digit():
    """
    All same last digit: nums = [21, 31, 41]
    Last digits: 1, 1, 1
    First digits: 2, 3, 4
    - (0,1): gcd(2,1)=1, beautiful
    - (0,2): gcd(2,1)=1, beautiful
    - (1,2): gcd(3,1)=1, beautiful
    Total: 3 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([21, 31, 41])
    print(f"Test [21, 31, 41]: {result}")
    assert result == 3, f"Expected 3 for [21, 31, 41], got {result}"

def test_large_array():
    """
    Larger array: nums = [31, 25, 72, 79, 74]
    First digits: 3, 2, 7, 7, 7
    Last digits: 1, 5, 2, 9, 4
    - (0,1): gcd(3,5)=1, beautiful
    - (0,2): gcd(3,2)=1, beautiful
    - (0,3): gcd(3,9)=3, not beautiful
    - (0,4): gcd(3,4)=1, beautiful
    - (1,2): gcd(2,2)=2, not beautiful
    - (1,3): gcd(2,9)=1, beautiful
    - (1,4): gcd(2,4)=2, not beautiful
    - (2,3): gcd(7,9)=1, beautiful
    - (2,4): gcd(7,4)=1, beautiful
    - (3,4): gcd(7,4)=1, beautiful
    Total: 7 beautiful pairs
    """
    sol = Solution()
    result = sol.countBeautifulPairs([31, 25, 72, 79, 74])
    print(f"Test [31, 25, 72, 79, 74]: {result}")
    assert result == 7, f"Expected 7 for [31, 25, 72, 79, 74], got {result}"

if __name__ == "__main__":
    print("Running tests for solution_36 (number-of-beautiful-pairs)...\n")
    
    test_example1()
    test_single_element()
    test_all_coprime()
    test_none_coprime()
    test_two_elements()
    test_two_elements_not_coprime()
    test_multi_digit_numbers()
    test_mixed_pairs()
    test_all_same_first_digit()
    test_all_same_last_digit()
    test_large_array()
    
    print("\nAll tests passed!")