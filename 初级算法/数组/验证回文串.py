'''
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
'''

def isPalindrome(s: str) -> bool:
    t = ''
    for i in s:
        if i >= 'A' and i <= 'Z':
            t += chr(ord(i) + 32)
        elif i >= 'a' and i <= 'z' or i >= '0' and i <= '9':
            t += i
    for i in range(len(t) // 2):
        if t[i] != t[len(t) - i - 1]:
            return False
    return True