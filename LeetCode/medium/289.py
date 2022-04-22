from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # if board[i][j] < 2 live neighbours, dead
        # if board[i][j] has 2 or 3 live neighbors, remains alive
        # if board[i][j] has > 3 live neighbors, dead
        # if dead board[i][j] has 3 live neighbors, becomes alive
        
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                cnt = 0
                if (i > 0): # check top
                    cnt += 1 if board[i - 1][j] > 0 else 0
                    if (j > 0):
                        cnt += 1 if board[i - 1][j - 1] > 0 else 0
                    if (j < n - 1):
                        cnt += 1 if board[i - 1][j + 1] > 0 else 0
                    
                if (i < m - 1): # check bottom
                    cnt += 1 if board[i + 1][j] > 0 else 0
                    if (j > 0):
                        cnt += 1 if board[i + 1][j - 1] > 0 else 0
                    if (j < n - 1):
                        cnt += 1 if board[i + 1][j + 1] > 0 else 0

                if (j > 0): # check left 
                    cnt += 1 if board[i][j - 1] > 0 else 0
                    
                if (j < n - 1): # check right
                    cnt += 1 if board[i][j + 1] > 0 else 0
                
                if board[i][j] == 1:
                    if (cnt < 2 or cnt > 3):
                        board[i][j] = 2  # 2 if once alive is now dead
                else:
                    if (cnt == 3):
                        board[i][j] = -1  # -1 if once dead is now alive

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1


nums = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(nums)
print(nums)