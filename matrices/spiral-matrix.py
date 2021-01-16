class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if matrix is None or len(matrix) == 0:
            return res
        
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            
            for i in range(top,bottom):
                res.append(matrix[i][right])
                
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
        
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        
        if left == right and top == bottom:
            res.append(matrix[top][left])
        
        elif left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[i][left])
        
        elif top == bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
        
        return res
