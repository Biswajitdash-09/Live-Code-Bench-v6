def solve():
    import sys
    input_data = sys.stdin.read().split()
    idx = 0
    
    t = int(input_data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        a = list(map(int, input_data[idx:idx+n]))
        idx += n
        
        # Find the index of the minimum element
        min_idx = 0
        for i in range(1, n):
            if a[i] < a[min_idx]:
                min_idx = i
        
        # Add 1 to the minimum digit to maximize the product
        a[min_idx] += 1
        
        # Calculate the product
        product = 1
        for num in a:
            product *= num
        
        print(product)

solve()