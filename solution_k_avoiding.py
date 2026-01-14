def minimumSum(n, k):
    """
    Returns the minimum possible sum of a k-avoiding array of length n.
    A k-avoiding array has no two distinct elements that sum to k.
    """
    selected = set()
    result = []
    
    # Start from the smallest positive integer
    current = 1
    
    while len(result) < n:
        check = k - current
        
        # Check if including current would create a pair summing to k
        if check not in selected:
            selected.add(current)
            result.append(current)
        
        current += 1
    
    return sum(result)

# Test with the example
print(minimumSum(5, 4))  # Expected output to be verified