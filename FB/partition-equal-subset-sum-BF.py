class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        return self.partitionHelper(nums, 0, 0, sum(nums))
        
    
    def partitionHelper(self, nums, index, curSum, total):
        if curSum * 2 == total:
            return True
        
        if curSum > total // 2 or index >= len(nums):
            return False
        
        return self.partitionHelper(nums, index + 1, curSum, total) or self.partitionHelper(nums, index + 1, curSum + nums[index], total)
