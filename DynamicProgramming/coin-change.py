class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for i in range(amount+1)]
        dp[0] = 0
        
        for i in range(len(dp)):
            for denom in coins:
                if denom <= i:
                    dp[i] = min(dp[i], 1 + dp[i - denom])
        return dp[-1] if dp[-1] != float("inf") else -1
