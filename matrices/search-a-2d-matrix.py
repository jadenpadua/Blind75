class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * cols - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_element = matrix[mid // cols][mid % cols]
            
            if mid_element == target:
                return True
            elif target < mid_element:
                right = mid - 1
            elif target > mid_element:
                left = mid + 1
        
        return False
