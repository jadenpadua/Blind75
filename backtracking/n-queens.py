class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        self.generateSolutions(n, solutions, [])
        print(solutions)
        output = []
        
        for solution in solutions:
            board = []
            for value in solution:
                board_row = ""
                for i in range(n):
                    if value == i:
                        board_row += 'Q'
                    else:
                        board_row += '.'
                board.append(board_row[:])
            output.append(board[:])
        
        return output
    
    def generateSolutions(self,n, solutions, currentSolution):
        if self.conflict(currentSolution) == True:
            return
        else:
            if len(currentSolution) == n:
                solutions.append(currentSolution[:])
    
        for i in range(n):
            currentSolution.append(i)
            self.generateSolutions(n, solutions, currentSolution)
            currentSolution.pop()
    
    def conflict(self, solution):
        if len(solution) == 1 or len(solution) == 0:
            return False
        
        else:
            row = len(solution) - 1
            col = solution[row]
            
            for i in range(len(solution)-1):
                if i == row or solution[i] == col or solution[i] + i == col + row or solution[i] - i == col - row:
                    return True
        return False
