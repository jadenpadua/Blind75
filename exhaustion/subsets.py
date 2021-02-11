class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for num in nums:
            subsets = subsets + [lst + [num] for lst in subsets]
        return subsets
