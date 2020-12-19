class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) == 1:
            return nums
        
        half = len(nums) // 2
        left = nums[:half]
        right = nums[half:]
        
        left = self.sortArray(left)
        right = self.sortArray(right)
        
        return sort(left,right)

def sort(a,b):
    temp = []
    while a and b:
        if a[0] <= b[0]:
            temp.append(a.pop(0))
        else:
            temp.append(b.pop(0))
        
    if a:
        temp += a

    else:
        temp += b
        
    return temp
