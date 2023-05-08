import sys

sys.stdin = open('input.txt')


def bomb(t):
    # 남은 폭탄 시간 깎기
    for ii in range(R):
        for jj in range(C):
            if 0 < arr[ii][jj] <= 3: arr[ii][jj] -= 1

    if t == 1: return
    # 폭탄 설치
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                arr[i][j] = 3

    bombed = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0:
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= R or nj < 0 or nj >= C: continue
                    bombed.append((ni, nj))
    # 터뜨림
    for bi, bj in bombed:
        arr[bi][bj] = -1



delta = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(4):
R, C, N = map(int, input().split())
arr = [[] for _ in range(R)]
for r in range(R):
    inp = list(input())
    for c in range(C):
        if inp[c] == '.': inp[c] = -1
        elif inp[c] == 'O': inp[c] = 3
    arr[r] = inp
# N = 19
limit = N
if N > 5 and (N % 4) == 3:
    limit = 1
elif N > 5 and (N % 4) == 1:
    limit = 3
elif not N % 2:
    limit = 2

# print(limit)
for time in range(1, limit+1):
    # print(time, '초')
    bomb(time)
    # print('-------------')

for rr in range(R):
    for cc in range(C):
        if arr[rr][cc] == -1:
            arr[rr][cc] = '.'
        else:
            arr[rr][cc] = 'O'

for a in arr:
    print(''.join(map(str, a)))