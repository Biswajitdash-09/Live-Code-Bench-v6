import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Initialize by starting with just the first element
        max_sum = a[0]
        current_sum = a[0]
        
        for i in range(1, n):
            # If adjacent elements have the same parity, we cannot extend
            # the current subarray. We must start fresh from the current element.
            if (a[i] % 2) == (a[i-1] % 2):
                current_sum = a[i]
            else:
                # Different parity - we can append this element to the valid subarray
                current_sum = current_sum + a[i]
            
            max_sum = max(max_sum, current_sum)
        
        print(max_sum)

if __name__ == "__main__":
    solve()