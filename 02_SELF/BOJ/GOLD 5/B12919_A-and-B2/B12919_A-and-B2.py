# 소요시간: 30분 이상 python 48ms
# - 거꾸로 거슬러 올라가야 시간 초과가 안나는 문제이다
import sys

sys.stdin = open('input.txt')


def recur(curr):
    global res
    if res: return

    if curr == S:
        res = 1
        return
    if len(curr) < len(S): return

    if curr[-1] == 'A': recur(curr[:-1])
    if curr[0] == 'B': recur(curr[::-1][:-1])


# for _ in range(3):
S = list(input())
T = list(input())
lenT = len(T)
res = 0
recur(T)
print(res)

