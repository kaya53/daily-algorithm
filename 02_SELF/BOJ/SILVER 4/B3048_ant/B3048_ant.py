# 소요시간 30분 python 40ms

import sys

sys.stdin = open('input.txt')

def solution():
    n1, n2 = map(int, input().split())
    m = n1+n2
    ants = []
    for k in input():
        ants.insert(0, (k, 0))
    for z in input():
        ants.append((z, 1))

    time = min(m-1, int(input()))

    for t in range(1, time+1):
        cand = []
        i = 0
        while i < m-1:
            if ants[i][1] == 0 and ants[i+1][1] == 1:
                cand.append((i, i+1))
                i += 2
            else: i += 1

        for i1, i2 in cand:
            ants[i1], ants[i2] = ants[i2], ants[i1]

    ans = []
    for c, d in ants:
        ans.append(c)
    return ''.join(ans)


# for _ in range(3):
print(solution())
