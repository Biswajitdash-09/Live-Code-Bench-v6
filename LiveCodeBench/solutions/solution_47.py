def getLongestSubstring(x, y, z):
    # Try different strategies and return the maximum valid length
    max_len = 0
    
    # Strategy 1: Alternate A and B groups
    # Use AB as boundary between AA and BB groups
    def try_canonical(ab_as_separator):
        aa_used = 0
        bb_used = 0
        ab_used = 0
        s = []
        
        while aa_used < x and bb_used < y and (aa_used + bb_used < x + y):
            if not s or s[-1].startswith('B'):
                if bb_used < y:
                    s.append("BB")
                    bb_used += 1
                elif aa_used < x:
                    s.append("AA")
                    aa_used += 1
                else:
                    break
            else:
                if aa_used < x:
                    s.append("AA")
                    aa_used += 1
                elif bb_used < y:
                    s.append("BB")
                    bb_used += 1
                else:
                    break
            
            if ab_as_separator and ab_used < z:
                s.append("AB")
                ab_used += 1
        
        # Add remaining ABs
        for _ in range(z - ab_used):
            s.append("AB")
            ab_used += 1
        
        # Try remaining AAs and BBs
        for _ in range(x - aa_used):
            s.append("AA")
            aa_used += 1
        
        for _ in range(y - bb_used):
            s.append("BB")
            bb_used += 1
        
        # Check validity
        result = ''.join(s)
        if "AAA" not in result and "BBB" not in result:
            return len(result)
        return 0
    
    # Try with and without AB as separator
    max_len = max(max_len, try_canonical(True))
    max_len = max(max_len, try_canonical(False))
    
    # Try greedy approach
    def try_greedy():
        s = []
        aa = x
        bb = y
        ab = z
        
        while aa > 0 or bb > 0 or ab > 0:
            added = False
            if ab > 0:
                if not s or s[-1].endswith('B'):
                    s.append("AB")
                    ab -= 1
                    added = True
            if not added and aa > 0:
                if not s or s[-1].startswith('B'):
                    s.append("AA")
                    aa -= 1
                    added = True
            if not added and bb > 0:
                if not s or s[-1].startswith('A'):
                    s.append("BB")
                    bb -= 1
                    added = True
            if not added:
                break
        
        result = ''.join(s)
        if "AAA" not in result and "BBB" not in result:
            return len(result)
        return 0
    
    max_len = max(max_len, try_greedy())
    
    # Fallback to simple construction
    result = 0
    if not result:
        # Simple bounding based on AB usage
        ab_can_add = min(z, abs(x - y))
        result = 2 * min(x, y)
        if x > y:
            result += 2 * min(x - y, z + z + 1)
        else:
            result += 2 * min(y - x, z + z + 1)
        result += 2 * (z - ab_can_add)
        max_len = max(max_len, result)
    
    return max_len