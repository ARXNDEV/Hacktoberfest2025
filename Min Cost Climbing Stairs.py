def min_cost_to_climb(cost):
    n = len(cost)
    if n == 1:
        return cost[0]
    # Initialize dp array
    dp = [0] * (n)
    # Starting points
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # The top beyond last step can be reached from either of the last two steps
    return min(dp[n-1], dp[n-2])
