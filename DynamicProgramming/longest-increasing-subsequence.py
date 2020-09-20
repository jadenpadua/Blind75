class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [-1,3,4,5,2,2,2,2]  
        n = len(nums)
        if n <= 1: return n
        
        memo = [1] * n
        LIS = 1
        
        for i in range(1, n):
            curr_LIS = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_LIS = max(curr_LIS, memo[j])
                    
            memo[i] = curr_LIS + 1
            LIS = max(LIS, memo[i])
        
        return LIS
