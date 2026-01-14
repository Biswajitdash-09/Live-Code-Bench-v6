def minCost(s: str) -> int:
    """
    Find the minimum cost to make all characters of binary string s equal.
    
    Operations:
    1. Choose index i and invert characters from index 0 to i (both inclusive), cost = i + 1
    2. Choose index i and invert characters from index i to n-1 (both inclusive), cost = n - i
    
    Key insight: Use recursion with memoization to track whether we've flipped the prefix
    containing index 0. If we've flipped it, all characters are inverted compared to original.
    
    Approach:
    - dp(i, first_is_flipped) = min cost to make suffix s[i:] uniform
    - If s[i] (possibly inverted) already equals the first character (possibly inverted),
      we continue without additional cost
    - Otherwise, we must flip either prefix 0...i or suffix i...n-1
    
    Time Complexity: O(n) with memoization
    Space Complexity: O(n) for memoization stack
    """
    n = len(s)
    
    # Memoization dictionary: (index, first_is_flipped) -> minimum cost
    memo = {}
    
    def dp(i: int, first_is_flipped: bool) -> int:
        """Find min cost to make suffix s[i:] uniform."""
        if i == n:
            # All characters are uniform, no more cost needed
            return 0
        
        if (i, first_is_flipped) in memo:
            return memo[(i, first_is_flipped)]
        
        # Get the actual value of s[0] (inverted if we've flipped the prefix)
        first_val = 0 if s[0] == '0' else 1
        if first_is_flipped:
            first_val = 1 - first_val
        
        # Get the actual value of s[i] (inverted if we've flipped the prefix)
        curr_val = 0 if s[i] == '0' else 1
        if first_is_flipped:
            curr_val = 1 - curr_val
        
        if curr_val == first_val:
            # Already matches first character, continue
            result = dp(i + 1, first_is_flipped)
        else:
            # Must make s[i] equal to first_val by flipping
            # Option 1: Flip prefix [0, i], cost = i + 1
            # This flips the entire prefix, so first_is_flipped becomes True
            flip_prefix_cost = (i + 1) + dp(i + 1, True)
            
            # Option 2: Flip suffix [i, n-1], cost = n - i
            # This flips the suffix only, but these characters were already inverted
            # relative to original, so we effectively unflip them
            # Since first_is_flipped is True, we flip to make first_is_flipped = True still
            # Actually, let me reconsider...
            
            # If first_is_flipped is False (original state):
            #   - Flip suffix [i, n-1], these characters get inverted
            #   - They were same as original, now they're inverted
            #   - If we check them in future, they still have first_is_flipped = False
            #   
            # If first_is_flipped is True (already flipped once):
            #   - Flip suffix [i, n-1], these characters get inverted (again)
            #   - They were inverted, now they're back to original
            #   - If we check them in future, they still have first_is_flipped = True
            #   - But wait, they're now equal to original, which means
            #     they're inverted relative to our tracking?
            # 
            # Actually, I think the simpler approach is:
            # - When we flip suffix [i, n-1], we invert characters s[i...n-1]
            # - This doesn't change the first_is_flipped flag
            # - Because first_is_flipped only tracks whether s[0] has been flipped
            # - And flipping the suffix doesn't include s[0]
            
            flip_suffix_cost = (n - i) + dp(i + 1, first_is_flipped)
            
            result = min(flip_prefix_cost, flip_suffix_cost)
        
        memo[(i, first_is_flipped)] = result
        return result
    
    # Try both cases: making all characters 0 or all characters 1
    # Case 1: Make all characters equal to s[0] (no initial flip)
    case1 = dp(1, False)
    
    # Case 2: Flip prefix [0, 0] first, so all characters are equal to 1 - s[0]
    case2 = 1 + dp(1, True)
    
    return min(case1, case2)