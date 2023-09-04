import sys

sys.stdin = open('input.txt')

N, D, K, C = map(int, input().split())
belt = [int(input()) for _ in range(N)]
belt = belt + belt[:K-1]

s = belt[:K]
mmax = 0
for i in range(N):
    if i == 0:
        now = set(s + [C])
    else:
        s = s[1:] + [belt[i+K-1]]
        now = set(s + [C])
    if mmax < len(now):
        # print(now)
        mmax = len(now)
print(mmax)