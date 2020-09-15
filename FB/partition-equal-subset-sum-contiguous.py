class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        splitPoint = self.findSplitPoint(nums)
    
        if splitPoint == -1 or splitPoint == len(nums):
            return "Cannot Split"
        
        else:
            return (nums[splitPoint:], nums[:splitPoint])
        
        
    def findSplitPoint(self, nums):
        
        left_sum = sum(nums)
        right_sum = 0
        
        for i in reversed(range(len(nums))):
            right_sum += nums[i]
            left_sum -= nums[i]
            
            if right_sum == left_sum:
                return i
            
        return -1
