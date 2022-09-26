'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。
'''


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in t:
        if i in d:
            d[i] -= 1
            if d[i] < 0:
                return False
        else:
            return False
    return True