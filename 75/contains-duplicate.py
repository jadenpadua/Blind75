class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}
        for num in nums:
            if num in hashSet:
                return True
            hashSet[num] = True
        return False
    
