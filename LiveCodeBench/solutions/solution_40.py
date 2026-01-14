def makeIntZero(num1, num2):
    for k in range(1, 62):
        target = num1 - k * num2
        if target < 0:
            continue
        # Check if we can represent target as sum of k powers of 2
        # Each 2^i can contribute i+1 "budget" (splitting into 2^0, 2^0, ..., 2^0)
        popcount = bin(target).count('1')
        # Extra budget calculation
        extra = 0
        temp = target
        i = 0
        while temp:
            if temp & 1:
                extra += i
            temp >>= 1
            i += 1
        if popcount <= k <= popcount + extra:
            return k
    return -1