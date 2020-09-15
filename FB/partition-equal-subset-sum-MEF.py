class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        return self.partitionHelper(nums, 0, 0, sum(nums), {})
        
    
    def partitionHelper(self, nums, index, curSum, total, ht):
        
        currentState = str(index) + ":" + str(curSum)
        
        if currentState in ht:
            return ht[currentState]
        
        
        if curSum * 2 == total:
            return True
        
        if curSum > total // 2 or index >= len(nums):
            return False
        
        foundPartition = self.partitionHelper(nums, index + 1, curSum, total, ht) or self.partitionHelper(nums, index + 1, curSum + nums[index], total, ht)
        
        ht[currentState] = foundPartition
        
        
        return foundPartition
