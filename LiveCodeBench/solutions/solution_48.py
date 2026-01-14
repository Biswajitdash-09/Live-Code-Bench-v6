def minimizeStringLength(words):
    """
    Minimize the length of concatenated strings using the join operation.
    join(x, y) removes one char if x[-1] == y[0].
    """
    n = len(words)
    
    # dp[(first_char, last_char)] = min_length
    # Initialize with first word
    dp = {(words[0][0], words[0][-1]): len(words[0])}
    
    for i in range(1, n):
        word = words[i]
        new_dp = {}
        
        for (str_first, str_last), length in dp.items():
            # Option 1: join(current_str, word)
            if str_last == word[0]:
                new_len = length + len(word) - 1  # Remove one overlapping char
            else:
                new_len = length + len(word)
            new_key = (str_first, word[-1])
            if new_key not in new_dp or new_len < new_dp[new_key]:
                new_dp[new_key] = new_len
            
            # Option 2: join(word, current_str)
            if word[-1] == str_first:
                new_len = length + len(word) - 1  # Remove one overlapping char
            else:
                new_len = length + len(word)
            new_key = (word[0], str_last)
            if new_key not in new_dp or new_len < new_dp[new_key]:
                new_dp[new_key] = new_len
        
        dp = new_dp
    
    return min(dp.values())

# Test with provided example
if __name__ == "__main__":
    # Example from problem
    words1 = ["aa", "ab", "bc"]
    print(f"Test 1: {words1} -> {minimizeStringLength(words1)}")  # Expected: 4
    
    # Additional test cases
    words2 = ["ab", "ba"]
    print(f"Test 2: {words2} -> {minimizeStringLength(words2)}")  # Expected: 2
    
    words3 = ["a", "b", "c"]
    print(f"Test 3: {words3} -> {minimizeStringLength(words3)}")  # Expected: 3
    
    words4 = ["ab", "bc", "ca"]
    print(f"Test 4: {words4} -> {minimizeStringLength(words4)}")  # Expected: 3 (abcabc -> abca with overlaps)