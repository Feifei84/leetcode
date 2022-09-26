'''
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果needle 不是 haystack 的一部分，则返回 -1 。
'''


def strStr(haystack: str, needle: str) -> int:
    j = haystack.find(needle[0], 0, len(haystack))
    while j + len(needle) <= len(haystack):
        if j == -1:
            return -1
        for i, s in enumerate(needle):
            if s != haystack[i + j]:
                break
            elif i == len(needle) - 1:
                return j
        j = haystack.find(needle[0], j + 1, len(haystack))
    return -1

# BM算法
def strStr(haystack: str, needle: str) -> int:
    i = len(needle) - 1
    while i < len(haystack):
        for j in range(len(needle)):
            if haystack[i - j] != needle[len(needle) - j - 1]:
                k = needle.rfind(haystack[i], 0, len(needle) - 1)
                # if k == -1:
                #    i = i + len(needle)
                # else:
                #   i = i + len(needle) - k - 1
                i = i + len(needle) - k - 1
                break
            elif j == len(needle) - 1:
                return i - j
    return -1