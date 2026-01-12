import sys

def solve():
    input = sys.stdin.read().split()
    idx = 0
    t = int(input[idx])
    idx += 1
    
    results = []
    
    for _ in range(t):
        n = int(input[idx])
        idx += 1
        a = list(map(int, input[idx:idx+n]))
        idx += n
        
        # Compute prefix sums
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + a[i]
        
        max_diff = 0
        
        # For each k from 1 to n
        for k in range(1, n + 1):
            if n % k != 0:
                continue
            
            # Calculate sum for each truck
            num_trucks = n // k
            truck_sums = []
            
            for truck in range(num_trucks):
                start = truck * k
                end = start + k
                truck_sum = prefix[end] - prefix[start]
                truck_sums.append(truck_sum)
            
            # Max absolute difference for this k
            current_diff = max(truck_sums) - min(truck_sums)
            max_diff = max(max_diff, current_diff)
        
        results.append(max_diff)
    
    print('\n'.join(map(str, results)))

solve()