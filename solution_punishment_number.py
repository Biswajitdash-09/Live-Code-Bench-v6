def can_form_partition(s, target, index, current_sum):
    """
    Helper function to check if we can partition string s to sum to target.
    
    Args:
        s: The string representation of i*i
        target: The target value (which is i)
        index: Current index in the string
        current_sum: Current sum of selected numbers
    
    Returns:
        bool: True if a valid partition exists
    """
    if current_sum > target:
        return False
    
    if index == len(s):
        return current_sum == target
    
    # Try taking different lengths of substring starting at index
    for end in range(index + 1, len(s) + 1):
        next_val = int(s[index:end])
        if can_form_partition(s, target, end, current_sum + next_val):
            return True
    
    return False


def punishmentNumber(n):
    """
    Returns the sum of the squares of all integers i (1 <= i <= n) such that
    i*i can be partitioned into contiguous substrings that sum to i.
    
    Args:
        n: A positive integer
    
    Returns:
        int: The punishment number of n
    """
    total = 0
    
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)
        
        # Check if square_str can be partitioned to sum to i
        if can_form_partition(square_str, i, 0, 0):
            total += square
    
    return total


# Optimized version with memoization
def can_form_partition_memo(s, target, index, current_sum, memo):
    """
    Memoized version of can_form_partition.
    """
    state = (index, current_sum)
    if state in memo:
        return memo[state]
    
    if current_sum > target:
        memo[state] = False
        return False
    
    if index == len(s):
        result = (current_sum == target)
        memo[state] = result
        return result
    
    for end in range(index + 1, len(s) + 1):
        next_val = int(s[index:end])
        if can_form_partition_memo(s, target, end, current_sum + next_val, memo):
            memo[state] = True
            return True
    
    memo[state] = False
    return False


def punishmentNumberOptimized(n):
    """
    Optimized version of punishmentNumber with memoization.
    """
    total = 0
    
    for i in range(1, n + 1):
        square = i * i
        square_str = str(square)
        memo = {}
        
        if can_form_partition_memo(square_str, i, 0, 0, memo):
            total += square
    
    return total