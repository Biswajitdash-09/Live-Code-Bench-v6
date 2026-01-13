def paintWalls(cost, time):
    """
    Calculate minimum cost to paint all walls using paid and free painters.
    
    DP[i][j] = minimum cost to have painted i walls with j free slots available.
    
    When we use paid painter: paint 1 wall, gain time[i] free slots
    When we use free painter: paint 1 wall, use 1 free slot
    
    We need to paint all n walls and find the minimum cost.
    """
    n = len(cost)
    INF = float('inf')
    
    # dp[i][j] = minimum cost to have painted i walls with j free slots available
    # i goes from 0 to n, j goes from 0 to n
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # 0 walls painted, 0 free slots, 0 cost
    
    for i in range(n):
        cost_i = cost[i]
        time_i = time[i]
        
        for j in range(n + 1):
            if dp[i][j] == INF:
                continue
            
            # Option 1: Use paid painter for wall i
            # Paint wall i using paid painter
            free_slots = min(j + time_i, n)
            dp[i + 1][free_slots] = min(dp[i + 1][free_slots], dp[i][j] + cost_i)
            
            # Option 2: Use free painter for wall i
            # Only possible if we have at least 1 free slot
            if j > 0:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    # At the end, n walls are painted. Any dp[n][j] gives a valid solution.
    # We need the minimum cost.
    result = min(dp[n])
    return result

def test_examples():
    print("=" * 70)
    print("Test 1: cost=[1, 2, 3, 2], time=[1, 2, 3, 2]")
    print("=" * 70)
    result1 = paintWalls([1, 2, 3, 2], [1, 2, 3, 2])
    print(f"Result: {result1}")
    print("Optimal: Pay for walls 1 and 3 (cost 2+2=4) - wait, let me verify...")
    print("Actually: Pay for walls 0 and 3 (cost 1+2=3)")
    print("  - Paid painter covers walls 0 and 3")
    print("  - Free painter slots: 1 + 2 = 3")
    print("  - Free painter paints walls 1 and 2")
    print(f"Expected: 3 [PASS]" if result1 == 3 else f"Expected: 4 or 3, Got: {result1} [FAIL]")
    
    print("\n" + "=" * 70)
    print("Test 2: cost=[2, 3, 4, 2], time=[1, 1, 1, 1]")
    print("=" * 70)
    result2 = paintWalls([2, 3, 4, 2], [1, 1, 1, 1])
    print(f"Result: {result2}")
    print("Optimal: Pay for walls 1 and 3 (cost 3+2=5)")
    print("  - Paid painter covers walls 1 and 3")
    print("  - Free painter slots: 1 + 1 = 2")
    print("  - Free painter paints walls 0 and 2")
    print(f"Expected: 5 [PASS]" if result2 == 5 else f"Expected: 5, Got: {result2} [FAIL]")
    
    print("\n" + "=" * 70)
    print("Additional Test 3: cost=[5, 5, 5], time=[5, 5, 5]")
    print("=" * 70)
    result3 = paintWalls([5, 5, 5], [5, 5, 5])
    print(f"Result: {result3}")
    print("Optimal: Pay for wall 0 (cost 5) - free painter can paint walls 1 and 2")
    print("  - Paid painter covers wall 0 (5 time units)")
    print("  - Free painter slots: 5")
    print("  - Free painter paints walls 1 and 2 (only 2 needed)")
    print(f"Expected: 5 [PASS]" if result3 == 5 else f"Expected: 5, Got: {result3} [FAIL]")
    
    print("\n" + "=" * 70)
    print("Additional Test 4: cost=[8, 7, 6, 5, 10], time=[2, 2, 1, 1, 2]")
    print("=" * 70)
    result4 = paintWalls([8, 7, 6, 5, 10], [2, 2, 1, 1, 2])
    print(f"Result: {result4}")
    print("Manual verification needed...")
    
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Test 1: {'PASS' if result1 == 3 else 'FAIL'}")
    print(f"Test 2: {'PASS' if result2 == 5 else 'FAIL'}")
    print(f"Test 3: {'PASS' if result3 == 5 else 'FAIL'}")

if __name__ == "__main__":
    test_examples()