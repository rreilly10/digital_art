def levenshtein_distance(s1, s2):
    m = len(s1) + 1
    n = len(s2) + 1
    dp = [[0 for j in range(n)] for i in range(m)]

    for i in range(1, m):
        dp[i][0] = i

    for j in range(1, n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    return dp[m - 1][n - 1]
