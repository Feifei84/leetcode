'''
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231, 231− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231− 1 的整数应该被固定为 231− 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
'''

# 此题官方采用确定有限状态机

class Automaton:
    def __init__(self):
        self.state = "S"
        self.sign = 1
        self.ans = 0
        self.table = {
            'S': ['S', 'number', 'sign', 'E'],
            'sign': ['E', 'number', 'E', 'E'],
            'number': ['E', 'number', 'E', 'E'],
            'E': ['E', 'E', 'E', 'E']
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        elif c.isdigit():
            return 1
        elif c == '+' or c == '-':
            return 2
        else:
            return 3

    def get(self,c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, 2**31 - 1) if self.sign == 1 else min(self.ans, 2**31)
        elif self.state == 'sign':
            self.sign = 1 if c == '+' else -1

def myAtoi(s: str) -> int:
    automaton = Automaton()
    for c in s:
        automaton.get(c)
    return automaton.sign * automaton.ans

# 更简单的解法
# 作者：QQqun902025048
# 链接：https://leetcode.cn/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/
def myAtoi_V2(s: str) -> int:
    import re
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
'''
^：匹配字符串开头
[\+\-]：代表一个+字符或-字符
?：前面一个字符可有可无
\d：一个数字
+：前面一个字符的一个或多个
'''
myAtoi_V2('  123  424')