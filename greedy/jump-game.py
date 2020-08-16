class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGood = len(nums) - 1
        for i in reversed(range(len(nums))):
            if i + nums[i] >= lastGood:
                lastGood = i
        
        return lastGood == 0
