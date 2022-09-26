'''
给定一个 n×n 的二维矩阵matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
import numpy


def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    import numpy
    matrix2 = numpy.rot90(matrix, -1)
    for i in range(len(matrix)):
        matrix[i] = list(matrix2[i])
def rotate_V2(matrix: list[list[int]]) -> None:
    j=0
    for i in zip(*matrix[::-1]):
        matrix[j]=i
        j+=1


def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]
    # 不能写成 matrix = matrix_new
    matrix[:] = matrix_new

def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # 水平翻转
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
    # 主对角线翻转
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotate_V2(matrix)