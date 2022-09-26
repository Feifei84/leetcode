'''
给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
'''


def firstUniqChar(s: str) -> int:
    for i in range(len(s)):
        if s.find(s[i]) == s.rfind(s[i]):
            return i
    return -1