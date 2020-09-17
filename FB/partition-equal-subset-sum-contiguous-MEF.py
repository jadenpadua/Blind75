class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        left = 0
        right = len(nums) - 1

        leftSum = nums[0]
        rightSum = nums[len(nums)-1]
        
        while left < right:
            
            if leftSum == rightSum:
                break
            
            elif rightSum > leftSum:
                leftSum += nums[left]
                left += 1
            
            else:
                rightSum += nums[right]
                right -= 1
        
        print([nums[right:], nums[:left+1]])
