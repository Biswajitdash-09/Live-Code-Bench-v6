class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """
        Find the minimum number of extra characters when breaking a string
        into non-overlapping substrings from a dictionary.
        
        Uses dynamic programming where dp[i] represents the minimum extra
        characters in the prefix s[0:i].
        
        Args:
            s: The input string
            dictionary: List of valid words
        
        Returns:
            Minimum number of extra characters
        """
        n = len(s)
        
        # Convert dictionary to a set for O(1) lookup
        word_set = set(dictionary)
        
        # dp[i] = minimum extra characters in s[0:i]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # No characters means no extra characters
        
        # Fill the dp table
        for i in range(1, n + 1):
            # Option 1: Leave s[i-1] as an extra character
            dp[i] = dp[i-1] + 1
            
            # Option 2: Try to end a word at position i
            # Check all possible word lengths
            for word in dictionary:
                word_len = len(word)
                if word_len <= i and s[i-word_len:i] == word:
                    # If we can form this word, don't add extra characters
                    dp[i] = min(dp[i], dp[i-word_len])
        
        return dp[n]

if __name__ == "__main__":
    solution = Solution()
    
    # Test with provided example
    s1 = "leetscode"
    dictionary1 = ["leet","code","leetcode"]
    result1 = solution.minExtraChar(s1, dictionary1)
    print(f"Test 1: s = \"{s1}\", dictionary = {dictionary1}")
    print(f"Result: {result1}")
    print(f"Expected: 1 (match 'leet' and 'code', leaving 's' as extra)")
    print()
    
    # Test with sayhelloworld
    s2 = "sayhelloworld"
    dictionary2 = ["hello","world"]
    result2 = solution.minExtraChar(s2, dictionary2)
    print(f"Test 2: s = \"{s2}\", dictionary = {dictionary2}")
    print(f"Result: {result2}")
    print(f"Expected: 3 (match 'hello' and 'world', leaving 'say' as extra)")
    print()
    
    # Test with exact match
    s3 = "leetcode"
    dictionary3 = ["leet","code","leetcode"]
    result3 = solution.minExtraChar(s3, dictionary3)
    print(f"Test 3: s = \"{s3}\", dictionary = {dictionary3}")
    print(f"Result: {result3}")
    print(f"Expected: 0 (whole string matches)")
    print()
    
    # Test with all single characters
    s4 = "abc"
    dictionary4 = ["a","b","c"]
    result4 = solution.minExtraChar(s4, dictionary4)
    print(f"Test 4: s = \"{s4}\", dictionary = {dictionary4}")
    print(f"Result: {result4}")
    print(f"Expected: 0")
    print()
    
    # Test with no matches
    s5 = "xyz"
    dictionary5 = ["ab","cd"]
    result5 = solution.minExtraChar(s5, dictionary5)
    print(f"Test 5: s = \"{s5}\", dictionary = {dictionary5}")
    print(f"Result: {result5}")
    print(f"Expected: 3 (no matches, all characters are extra)")
    print()
    
    # Test with single character match
    s6 = "a"
    dictionary6 = ["a"]
    result6 = solution.minExtraChar(s6, dictionary6)
    print(f"Test 6: s = \"{s6}\", dictionary = {dictionary6}")
    print(f"Result: {result6}")
    print(f"Expected: 0")
    print()
    
    # Test with single character no match
    s7 = "a"
    dictionary7 = ["b"]
    result7 = solution.minExtraChar(s7, dictionary7)
    print(f"Test 7: s = \"{s7}\", dictionary = {dictionary7}")
    print(f"Result: {result7}")
    print(f"Expected: 1")