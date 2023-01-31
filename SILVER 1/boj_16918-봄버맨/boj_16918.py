import sys
import copy

sys.stdin = open('input.txt')

r, c, n = map(int, input().split())
initial = [[] for _ in range(r)]
full = [['O']*c for _ in range(r)]

bombed = copy.deepcopy(full)

for i in range(r):
    tmp = input()
    for elem in tmp:
        initial[i].append(elem)
# print(initial, full)
# ['.......', '...O...', '....O..', '.......', 'OO.....', 'OO.....']

# bombed 만들기
# 상하좌우 현재
di = [-1, 1, 0, 0, 0]
dj = [0, 0, -1, 1, 0]
for i in range(r):
    for j in range(c):
        if initial[i][j] == 'O':
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if (0 <= ni < r and 0 <= nj < c) and bombed[ni][nj] == 'O':
                    bombed[ni][nj] = '.'

if n % 4 == 0 or n%4 == 2:
    res = full
elif n % 4 == 1:
    res = initial
elif n % 4 == 3:
    res = bombed

for elem in res:
    print(*elem, sep='')