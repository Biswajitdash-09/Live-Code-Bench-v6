def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    num = input_data[0].strip()
    
    # Remove trailing zeros
    result = num.rstrip('0')
    
    # If result is empty (e.g., input was "0" or "000"), return "0"
    if not result:
        result = '0'
    
    print(result)

if __name__ == "__main__":
    solve()