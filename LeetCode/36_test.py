# from collections import defaultdict #普通dict返回keyerror，defaultdict根据dict的形式返回默认值
# class Solution:
#     def solveSudoku(self,board):
#         def could_place(value,row,col):#检查这个地方是已经在行列box中出现过
#             judge = value in rows[row] or value in cols[col] or boxes[box_index(row,col)]
#             return not judge

#         def place_number(value,row,col):
#             rows[row][value] += 1 #注意它最大就是1
#             cols[col][value] += 1
#             boxes[box_index(row,col)][value] += 1
#             #放置
#             board[row][col] = str(d)
#         def remove_number(value,row,col):
#             del rows[row][value]
#             del columns[col][d]
#             del boxes[box_index(row, col)][d]
#             board[row][col] = '.' 

row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字
print(row)

