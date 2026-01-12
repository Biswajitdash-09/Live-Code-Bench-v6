import sys

def solve() -> None:
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    results = []
    
    for _ in range(t):
        n = int(next(iterator))
        arr = [int(next(iterator)) for _ in range(n)]
        
        freq = {}
        for val in arr:
            freq[val] = freq.get(val, 0) + 1
        
        ans = 0
        if 1 in freq:
            ans += freq[1] * (freq[1] - 1) // 2
        
        if 2 in freq:
            ans += freq[2] * (freq[2] - 1) // 2
        
        if 1 in freq and 2 in freq:
            ans += freq[1] * freq[2]
        
        for val in freq:
            if val != 1 and val != 2:
                ans += freq[val] * (freq[val] - 1) // 2
        
        results.append(str(ans))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()