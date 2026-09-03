class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes =[set() for _ in range(9)] 

        for row in board:
            row_set = set()
            for cell in row:
                if cell == ".": continue
                elif cell in row_set: return False
                else: row_set.add(cell)   

        for col in zip(*board):
            col_set = set()
            for cell in col:
                if cell == ".": continue
                elif cell in col_set: return False
                else: col_set.add(cell)   


        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                b = i//3 * 3 + j//3
                if cell == ".": continue
                elif cell in boxes[b]: return False
                else: boxes[b].add(cell)

        return True