# 소요시간 1시간 pypy 116ms python 44ms
# - 어려운 문제는 아닌데 왜 이렇게 집중을 못하니....
# - 왼쪽에서 훑고, 훑었을 때 오른쪽 끝까지 안갔으면 오른쪽부터 다시 훑으면 되는 문제였음

import sys

sys.stdin = open('input.txt')

# for _ in range(4):
N, M = map(int, input().split())
board = list(map(int, input().split()))

res_ls = []
left = (0, board[0])
from_left = 0
for i in range(1, M):
    if board[i] >= left[1]:
        res_ls.append((left[0], i, min(left[1], board[i])))
        left = (i, board[i])
        from_left = i

if from_left != M-1:
    right = (M-1, board[M-1])
    for j in range(M-2, from_left-1, -1):
        if board[j] >= right[1]:
            res_ls.append((j, right[0], min(right[1], board[j])))
            right = (j, board[j])

ans = 0
for s, e, limit in res_ls:
    for j in range(s+1, e):
        m = limit - board[j]
        if m > 0: ans += m
print(ans)
