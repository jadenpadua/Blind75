class Solution(object):
    def gameOfLife(self, board):
        
        if not board or len(board[0]) == 0:
            return
        
        n = len(board)
        m = len(board[0])
        
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                count = 0
                for a in range(max(0, i-1), min(i+2, n)):
                    for b in range(max(0, j-1), min(j+2, m)):
                        if (a,b) != (i,j) and 1 <= board[a][b] <= 2:
                            count += 1
                
                if board[i][j] == 0:
                    if count == 3:
                        board[i][j] = 3
                
                else:
                    if count < 2 or count > 3:
                        board[i][j] = 2
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2:
                    board[i][j] = 0
                    
                elif board[i][j] == 3:
                    board[i][j] = 1
        
        return board
