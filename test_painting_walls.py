def paintWalls(cost, time):
    """
    Calculate minimum cost to paint all walls using paid and free painters.
    
    Key insight: Let dp[i][j] = minimum cost to paint walls from index i with
    j available free painter slots.
    
    Actually, let's define it differently:
    dp[i][j] = minimum cost to have painted i walls using j paid walls.
    Number of free walls painted = i - j
    Free slots available = sum of time for the j paid walls
    
    Constraint: total free slots >= number of free walls painted
    sum(time for paid walls) >= i - j
    
    This is complex. Let me think of a cleaner approach...
    
    Alternative formulation:
    Let dp[j] = minimum cost when we have j free painter slots available after
    processing all walls.
    After painting all n walls, we need to have painted all n.
    
    When we use paid painter for wall i: cost increases by cost[i], free slots increase by time[i]
    When we use free painter for wall i: cost unchanged, free slots decrease by 1
    
    We process n walls total. At the end, we must have painted all n walls.
    The constraint is: at minimum, we need enough free slots to cover the walls painted by free painter.
    This means: final free slots >= 0? No, that's not right.
    
    Actually, the issue is we need to track how many walls we've painted.
    
    Let me try a different formulation:
    dp[i][j] = minimum cost where i = number of walls painted, j = available free slots
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
            
            # Option 1: Use paid painter for wall i+1 (next wall)
            # Paint wall i+1 using paid painter
            free_slots = min(j + time_i, n)
            dp[i + 1][free_slots] = min(dp[i + 1][free_slots], dp[i][j] + cost_i)
            
            # Option 2: Use free painter for wall i+1
            # Only possible if we have at least 1 free slot
            if j > 0:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    # At the end, n walls are painted. Any dp[n][j] >= 0 gives a valid solution.
    # We need the minimum cost.
    result = min(dp[n])
    return result

def test_examples():
    print("=" * 60)
    print("Test 1: cost=[1, 2, 3, 2], time=[1, 2, 3, 2]")
    print("=" * 60)
    result1 = paintWalls([1, 2, 3, 2], [1, 2, 3, 2])
    print(f"\nResult: {result1}")
    print("Expected: 3 (pay for walls 1 and 3 with cost 2+2)")
    
    print("\n" + "=" * 60)
    print("Test 2: cost=[2, 3, 4, 2], time=[1, 1, 1, 1]")
    print("=" * 60)
    result2 = paintWalls([2, 3, 4, 2], [1, 1, 1, 1])
    print(f"\nResult: {result2}")
    print("Expected: 10 (pay for walls 0,1,2, leave 3 for free painter)")

if __name__ == "__main__":
    test_examples()