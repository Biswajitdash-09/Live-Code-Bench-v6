def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    n = int(input_data[0].strip())
    
    # Calculate 2*n and 3*n
    n2 = 2 * n
    n3 = 3 * n
    
    # Concatenate n, 2*n, and 3*n
    concatenated = str(n) + str(n2) + str(n3)
    
    # Check if the concatenated number is fascinating:
    # 1. Must have exactly 9 digits
    # 2. Must contain all digits from 1 to 9 exactly once
    # 3. Must not contain any 0s
    
    if len(concatenated) != 9:
        print("false")
        return
    
    # Check for any 0s
    if '0' in concatenated:
        print("false")
        return
    
    # Check if all digits 1-9 appear exactly once
    digit_count = {}
    for char in concatenated:
        digit_count[char] = digit_count.get(char, 0) + 1
    
    # Verify we have exactly one of each digit 1-9
    for digit in '123456789':
        if digit_count.get(digit, 0) != 1:
            print("false")
            return
    
    print("true")

if __name__ == "__main__":
    solve()