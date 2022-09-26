'''
请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字1-9在每一行只能出现一次。
数字1-9在每一列只能出现一次。
数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。

注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用'.'表示。
'''
import numpy as np
def isValidSudoku(lboard: list[list[str]]) -> bool:
    def is_twice(L) -> bool:
        L = sorted(str2num(L))
        for i in range(len(L) - 1):
            if L[i] == L[i + 1]:
                return True
        return False

    def str2num(L) -> list:
        num = []
        for i in L:
            if i != '.':
                num.append(int(i))
        return num
    lboard = np.array(lboard)
    for i in range(9):
        if is_twice(lboard[i]):
            return False
        if is_twice(lboard[:, i]):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if is_twice(np.reshape(lboard[i:i+3,j:j+3],(9))):
                return False
    return True


def isValidSudoku_V2(board: list[list[str]]) -> bool:
    for i in range(9):
        storage = set()
        length = 0
        for j in range(9):
            if board[i][j] == '.':
                continue
            storage.add(board[i][j])
            if length == len(storage):
                return False
            else:
                length += 1
    for i in range(9):
        storage = set()
        length = 0
        for j in range(9):
            if board[j][i] == '.':
                continue
            storage.add(board[j][i])
            if length == len(storage):
                return False
            else:
                length += 1
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            storage = set()
            length = 0
            for x in range(0, 3):
                for y in range(0, 3):
                    if board[i + x][j + y] == '.':
                        continue
                    storage.add(board[i + x][j + y])
                    if length == len(storage):
                        return False
                    else:
                        length += 1
    return True

print(isValidSudoku_V2([["8","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))