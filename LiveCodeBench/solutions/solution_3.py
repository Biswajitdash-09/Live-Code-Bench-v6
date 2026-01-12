import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        # Count character frequencies
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        # Count characters with odd frequency
        odd_count = sum(1 for v in freq.values() if v % 2 == 1)
        
        remaining_length = n - k
        
        if remaining_length % 2 == 0:
            # Need 0 odd characters after removal
            # To get 0 odd: remove 1 from each odd char (cost = odd_count),
            # then remove pairs from any even chars
            if k >= odd_count and (k - odd_count) % 2 == 0:
                results.append("YES")
            else:
                results.append("NO")
        else:
            # Need exactly 1 odd character after removal
            # We can achieve exactly 1 odd if:
            # - odd_count == 1 and k is even (remove from even groups only)
            # - odd_count > 1 and (k - odd_count) is even (remove 1 from all odd, then pairs)
            if odd_count == 1:
                if k % 2 == 0:
                    results.append("YES")
                else:
                    results.append("NO")
            else:
                if k >= odd_count and (k - odd_count) % 2 == 0:
                    results.append("YES")
                else:
                    results.append("NO")
    
    print("\n".join(results))

solve()