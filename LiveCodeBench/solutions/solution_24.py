def solve():
    n = int(input().strip())
    queries = eval(input().strip())
    
    nums = [0] * n
    count = 0
    result = []
    
    for index, color in queries:
        # First, check if the old value at index created any matches
        # and subtract them from count
        old_color = nums[index]
        
        if index > 0:
            if old_color == nums[index - 1] and old_color != 0:
                count -= 1
        
        if index < n - 1:
            if old_color == nums[index + 1] and old_color != 0:
                count -= 1
        
        # Now update the value
        nums[index] = color
        
        # Then check if the new value creates any matches
        # and add them to count
        if index > 0:
            if color == nums[index - 1] and color != 0:
                count += 1
        
        if index < n - 1:
            if color == nums[index + 1] and color != 0:
                count += 1
        
        result.append(count)
    
    return result

if __name__ == "__main__":
    result = solve()
    print(result)