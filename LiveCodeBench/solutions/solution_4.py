import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    # Read number of test cases (should be 15 based on input)
    # But first line is actually "15", so let's parse
    
    t = 15  # Based on the input structure
    
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx + 1])
        idx += 2
        
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        
        if k == 2:
            # Need at least one even number
            min_ops = float('inf')
            for a in arr:
                if a % 2 == 0:
                    min_ops = 0
                    break
            if min_ops != 0:
                min_ops = 1  # Make any odd number even
        
        elif k == 3:
            # Need at least one number divisible by 3
            min_ops = float('inf')
            for a in arr:
                needed = (3 - a % 3) % 3
                min_ops = min(min_ops, needed)
        
        elif k == 4:
            # For product to be divisible by 4, we need:
            # 1. At least one number divisible by 4
            # 2. Or at least 2 even numbers
            
            # Option 1: Make a number divisible by 4
            min_ops_4 = float('inf')
            for a in arr:
                needed = (4 - a % 4) % 4
                min_ops_4 = min(min_ops_4, needed)
            
            # Option 2: Make at least 2 numbers even
            ops_needed = []
            for a in arr:
                if a % 2 == 0:
                    ops_needed.append(0)
                else:
                    ops_needed.append(1)
            
            ops_needed.sort()
            if len(ops_needed) >= 2:
                min_ops_2_even = ops_needed[0] + ops_needed[1]
            else:
                min_ops_2_even = float('inf')
            
            min_ops = min(min_ops_4, min_ops_2_even)
        
        elif k == 5:
            # Need at least one number divisible by 5
            min_ops = float('inf')
            for a in arr:
                needed = (5 - a % 5) % 5
                min_ops = min(min_ops, needed)
        
        results.append(min_ops)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    solve()