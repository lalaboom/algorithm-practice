def solveSudoku(self, board: List[List[str]]) -> None:
    rows = [set(range(1,10)) for _ in range(9)]
    cols = [set(range(1,10)) for _ in range(9)]
    boxes = [set(range(1,10)) for _ in range(9)]
    empty = [] #应该放置数字的位置
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                rows[i].remove(val)
                cols[j].remove(val)
                boxes[(i // 3)*3 + j // 3].remove(val)
            else:
                empty.append((i,j))
    def backtrack(iter=0):
        if iter==len(empty): #递归终止条件
            return True
        i,j = empty[iter]
        boxes_index = (i // 3)*3 + j // 3
        for val in row[i] & col[j] & block[b]:
            row[i].remove(val)
            col[j].remove(val)
            boxes[boxes_index].remove(val)
            board[i][j] = str(val)
            if backtrack(iter+1):
                return True
            row[i].add(val)  # 回溯
            col[j].add(val)
            block[b].add(val)
        return False
    backtrack()