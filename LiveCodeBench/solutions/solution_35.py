def getSmallestString(s: str) -> str:
    """
    Return the lexicographically smallest string after performing exactly one operation
    where you can select any substring and decrement each character ('b'->'a', 'a'->'z').
    """
    result = []
    i = 0
    skip_count = 0  # Count of leading 'a's skipped
    
    # Skip leading 'a's since 'a' -> 'z' makes the string worse
    while i < len(s) and s[i] == 'a':
        result.append(s[i])
        i += 1
        skip_count += 1
    
    # Start the operation when we find first non-'a' character
    # Continue decrementing while it improves lexicographic order
    # (i.e., stop before we need to decrement 'a' to 'z')
    start_i = i  # Save where decrementing started
    while i < len(s) and s[i] != 'a':
        # Decrement the character
        result.append(chr(ord(s[i]) - 1))
        i += 1
    
    # Add the rest of the string unchanged
    while i < len(s):
        result.append(s[i])
        i += 1
    
    # If the result is the same as the original string,
    # it means we didn't perform the operation (all chars are 'a').
    # The best we can do is decrement the last 'a' to 'z'.
    original_len = len(s)
    if len(''.join(result)) == original_len and len(set(s)) == 1 and 'a' in s:
        # All characters are 'a', replace the last one with 'z'
        result = ['a'] * (original_len - 1) + ['z']
    
    return ''.join(result)