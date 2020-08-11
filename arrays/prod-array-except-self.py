class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * len(nums)
        multiplier = 1
        for i in range(len(nums)):
            prod[i] = prod[i] * multiplier
            multiplier = multiplier * nums[i]
            
        multiplier = 1
        for i in reversed(range(len(nums))):
            prod[i] = prod[i] * multiplier
            multiplier = multiplier * nums[i]
        
        return prod
