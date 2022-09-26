def kSimilarity(s1: str, s2: str) -> int:
    n = len(s1) - 1
    swap = 0
    cnt = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[i]:
                cnt += 1
                break
            elif s1[i] == s2[j] and s2[i] == s1[j]:
                swap += 1
                break
    return n - swap//2 - cnt + int(swap + cnt == len(s1))

def kSimilarity_V2(s1: str, s2: str) -> int:
    def count(s1: str, s2: str):
        i = 0
        while i < len(s1):
            if s1[i] == s2[i]:
                s1 = s1[:i] + s1[i + 1:]
                s2 = s2[:i] + s2[i + 1:]
            else:
                i += 1
        if len(s1) == 0:
            return 0
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j] and s2[i] == s1[j]:
                    s2 = s2[:i] + s1[i] + s2[i + 1:j] + s1[j] + s2[j + 1:]
                    return 1 + count(s1, s2)
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    s2 = s2[:i] + s2[j] + s2[i + 1:j] + s2[i] + s2[j + 1:]
                    return 1 + count(s1, s2)
    return count(s1, s2)


def kSimilarity_ANS(s1: str, s2: str) -> int:
    step, n = 0, len(s1)
    q, vis = [(s1, 0)], {s1}
    while True:
        tmp = q
        q = []
        for s, i in tmp:
            if s == s2:
                return step
            while i < n and s[i] == s2[i]:
                i += 1
            for j in range(i + 1, n):
                if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                    t = list(s)
                    t[i], t[j] = t[j], t[i]
                    t = ''.join(t)
                    if t not in vis:
                        vis.add(t)
                        q.append((t, i + 1))
        step += 1

print(kSimilarity_ANS("aabbccddee",
"cdacbeebad"))
