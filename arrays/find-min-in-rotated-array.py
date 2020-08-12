class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            
            elif nums[mid] > nums[right]:
                left = mid + 1
                
            else:
                right = mid - 1
        
        return nums[left]
