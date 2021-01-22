class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] *(n+1)
        for i in range(1, n+1):
            min_val = i
            j, sq = 1,1
            
            while sq <= i:
                min_val = min(min_val, 1 + dp[i-sq])
                j += 1
                sq = j*j
            dp[i] = min_val
            
        return dp[n]
