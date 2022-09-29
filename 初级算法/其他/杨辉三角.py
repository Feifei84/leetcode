'''
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
'''

def generate(numRows: int) -> list[list[int]]:
    ans = []
    for i in range(1, numRows + 1):
        ans.append([1])
        for j in range(1, i):
            if j == i-1:
                ans[i - 1].append(1)
            else:
                ans[i - 1].append(ans[i-2][j-1] + ans[i-2][j])
    return ans

def generate_V2(numRows: int) -> list[list[int]]:
    ans = []
    for i in range(numRows):
        ans.append([1])
        for j in range(1, i):
            ans[i].append(ans[i-1][j-1] + ans[i-1][j])
        if i > 0:
            ans[i].append(1)
    return ans

ans = generate_V2(5)
ans