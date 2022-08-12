class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # each row 1 - 9
        # each col 1 - 9
        # each 3 x 3 has 1 - 9
        n = len(board)

        # case 1: check rows
        for row in range(n):
            seen = set()
            for col in range(n):
                curr = board[row][col]
                if curr != ".":
                    if curr in seen:
                        return False
                    seen.add(curr)
        
        # case 2: check cols
        for col in range(n):
            seen = set()
            for row in range(n):
                curr = board[row][col]
                if curr != ".":
                    if curr in seen:
                        return False
                    seen.add(curr)
        
        # case 3: check 3 x 3
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        curr = board[row + i][col + j]
                        if curr != ".":
                            if curr in seen:
                                return False
                            seen.add(curr)
        
        return True
                        

            
    

board = [
    ["5","3","2",".","7",".",".",".","."]
    ,["6","4","1","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
print(Solution().isValidSudoku(board))