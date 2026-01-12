def solve():
    t = int(input())
    for _ in range(t):
        s = input().strip()
        target = "abc"
        
        # Count positions where characters don't match
        mismatches = []
        for i in range(3):
            if s[i] != target[i]:
                mismatches.append(i)
        
        # If 0 mismatches: already "abc" - YES
        # If 2 mismatches: can swap to fix - YES
        # If 1 or 3 mismatches: cannot fix with at most one swap - NO
        if len(mismatches) == 0 or len(mismatches) == 2:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()