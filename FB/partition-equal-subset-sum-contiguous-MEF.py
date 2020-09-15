class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        left = 0
        right = len(nums) - 1

        while left < right:
            
            if sum(nums[right:]) == sum(nums[:left+1]):
                
                return [nums[right:], nums[:left+1]]
            
            elif sum(nums[right:]) > sum(nums[:left+1]):
                
                left += 1
            
            else:
                right -= 1
                
        return -1        
