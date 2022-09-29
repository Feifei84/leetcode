'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

实现 MinStack 类:

MinStack() 初始化堆栈对象。
void push(int val) 将元素val推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
'''


class MinStack:
    def __init__(self):
        self.L = []

    def push(self, val: int) -> None:
        self.L.append(val)

    def pop(self) -> None:
        self.L.pop()

    def top(self) -> int:
        return self.L[-1]

    def getMin(self) -> int:
        return min(self.L)

class MinStack2:
    def __init__(self):
        self.L = []
        self.min = [2**31]

    def push(self, val: int) -> None:
        self.L.append(val)
        self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.L.pop()
        self.min.pop()

    def top(self) -> int:
        return self.L[-1]

    def getMin(self) -> int:
        return self.min[-1]