class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxSums = nums[:]
        maxSums[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            maxSums[i] = max(maxSums[i-1],maxSums[i-2] + nums[i])
        return maxSums[-1]
