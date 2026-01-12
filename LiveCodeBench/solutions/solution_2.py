import sys

def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, k = map(int, data[idx].split())
        idx += 1
        s = data[idx]
        idx += 1
        
        count = 0
        i = 0
        while i < n:
            if s[i] == 'B':
                count += 1
                i += k  # Skip k cells since we just made them white
            else:
                i += 1
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == "__main__":
    solve()