class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        globalMax = nums[0]
        for num in nums[1:]:
            currMax = max(currMax + num, num)
            globalMax = max(globalMax, currMax)
        
        return globalMax
