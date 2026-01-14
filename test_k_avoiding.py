def test_minimum_sum():
    print("Testing k-avoiding array minimum sum solution...")
    
    test_cases = [
        # (n, k, expected_output, description)
        (5, 4, None, "Example: n=5, k=4"),
        (2, 6, None, "Small array, large k"),
        (3, 5, None, "n=3, k=5"),
        (10, 7, None, "Larger array"),
        (1, 100, None, "Single element"),
        (100, 10, None, "Large n, small k"),
        (5, 100, None, "Small n, large k"),
        (10, 10, None, "n=k=10"),
    ]
    
    from solution_k_avoiding import minimumSum
    
    for n, k, expected, description in test_cases:
        result = minimumSum(n, k)
        print(f"{description}: n={n}, k={k} -> result={result}")
        
        # Verify the result is actually k-avoiding
        # Reconstruct the array (by re-running the algorithm)
        selected = set()
        arr = []
        current = 1
        while len(arr) < n:
            check = k - current
            if check not in selected:
                selected.add(current)
                arr.append(current)
            current += 1
        
        # Verify no pair sums to k
        is_valid = True
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == k:
                    is_valid = False
                    print(f"  ERROR: Found pair {arr[i]} + {arr[j]} = {k}")
                    break
        
        # Verify sum matches
        actual_sum = sum(arr)
        if result != actual_sum:
            print(f"  ERROR: Sum mismatch! result={result}, actual_sum={actual_sum}")
            is_valid = False
        
        if is_valid:
            print(f"  [OK] Valid k-avoiding array: {arr[:10]}{'...' if len(arr) > 10 else ''}")
        else:
            print(f"  [X] Invalid!")
        print()

if __name__ == "__main__":
    test_minimum_sum()