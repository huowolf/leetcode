#===============================================================================
# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
# 1.数字 1-9 在每一行只能出现一次。
# 2.数字 1-9 在每一列只能出现一次。
# 3.数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#===============================================================================
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #按行检测
        rowset=set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.': 
                    if board[i][j] not in rowset:
                        rowset.add(board[i][j])
                    else:
                        return False
            rowset.clear()
            
        #按列检测
        colset=set()        
        for i in range(9):
            for j in range(9):
                if board[j][i]!='.': 
                    if board[j][i] not in colset:
                        colset.add(board[j][i])
                    else:
                        return False 
            colset.clear()           

        #按3*3宫格检测
        cellset=set()
        for i in range(0,9,3):
            for j in range(0,9,3):
                #print(i,j)
                #(i,j)代表左上角的坐标
                for m in range(i,i+3):
                    for n in range(j,j+3):
                        if board[m][n]!='.':
                            if board[m][n] not in cellset:
                                cellset.add(board[m][n])
                            else:
                                return False
                cellset.clear()
        
        return True
                    
board=[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
r=Solution().isValidSudoku(board)
assert r==True
board=[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
r=Solution().isValidSudoku(board)
assert r==False