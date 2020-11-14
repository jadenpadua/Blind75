class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] not in hashTable:
                hashTable[target - nums[i]] = i
            else:
                return hashTable[nums[i]], i
        
        return -1, -1
