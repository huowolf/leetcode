# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(0,n//2):
            for j in range(i,n-1-i):
                
                temp=matrix[i][j]
                #上=左
                matrix[i][j]=matrix[n-1-j][i]
                #左=下
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                #下=右
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                #右=保存量
                matrix[j][n-1-i]=temp
        
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

Solution().rotate(matrix)
print(matrix)
assert matrix==[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

matrix =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
Solution().rotate(matrix)
print(matrix)
assert matrix==[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

