def sumImbalanceNumbers(nums):
    total = 0
    n = len(nums)
    
    for i in range(n):
        for j in range(i, n):
            subarray = nums[i:j+1]
            sorted_arr = sorted(subarray)
            gaps = 0
            for k in range(len(sorted_arr) - 1):
                if sorted_arr[k+1] - sorted_arr[k] > 1:
                    gaps += 1
            total += gaps
    
    return total