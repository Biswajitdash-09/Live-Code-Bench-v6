def paintWalls(cost, time):
    """
    Calculate minimum cost to paint all walls using paid and free painters.
    
    Problem: Given n walls with cost[i] and time[i], find minimum cost to paint all walls.
    - Paid painter: paints wall i in time[i] units, costs cost[i]
    - Free painter: paints any wall in 1 unit time, costs 0, but only available when paid painter is busy
    
    Key insight: When paid painter paints wall i for time[i] units, the free painter
    can paint time[i] walls during that same period.
    
    So if we paint k walls with the paid painter, the free painter can paint sum(time[i]) walls.
    Constraint: k + sum(time[i]) >= n (total walls must be painted)
    
    DP formulation: dp[i][j] = minimum cost to have painted i walls with j free slots available
    - i: number of walls painted so far (0 to n)
    - j: number of free painter slots available (0 to n)
    
    Transitions:
    1. Use paid painter for wall i: cost += cost[i], free_slots += time[i]
    2. Use free painter for wall i: if j > 0, free_slots -= 1
    
    Answer: min(dp[n][j]) for all j
    """
    n = len(cost)
    INF = float('inf')
    
    # dp[i][j] = minimum cost to have painted i walls with j free slots available
    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Initial state: 0 walls painted, 0 free slots, 0 cost
    
    for i in range(n):
        cost_i = cost[i]
        time_i = time[i]
        
        for j in range(n + 1):
            if dp[i][j] == INF:
                continue
            
            # Option 1: Use paid painter for wall i
            # Paint wall i using paid painter, gain time[i] free slots
            free_slots = min(j + time_i, n)
            dp[i + 1][free_slots] = min(dp[i + 1][free_slots], dp[i][j] + cost_i)
            
            # Option 2: Use free painter for wall i (only if we have slots)
            # Paint wall i using free painter, consume 1 free slot
            if j > 0:
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    # Return minimum cost to paint all n walls
    return min(dp[n])