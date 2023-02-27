import sys

sys.stdin = open('input.txt')


def board_num(i, j):
    if 0 <= i <= 2:
        board = 0
    elif 3 <= i <= 5:
        board = 3
    else:
        board = 6
    if 0 <= j <= 2:
        return board
    elif 3 <= j <= 5:
        return board + 1
    else:
        return board + 2


def backtrack(cnt):
    global res_ls
    if cnt == lenT:
        res_ls = list(choice)
        return

    ci, cj = target[cnt]
    for k in range(1, 10):  # 숫자 집어넣기
        if row[ci][k - 1]: continue
        if col[cj][k - 1]: continue
        bIdx = board_num(ci, cj)
        if square[bIdx][k - 1]: continue
        # 어디에도 안들어간 숫자가 있으면
        arr[ci][cj] = k
        row[ci][k-1] = col[cj][k-1] = square[bIdx][k-1] = 1
        choice[cnt] = k
        # 다음 턴 -> 다음 0인 곳으로 넘기기
        backtrack(cnt + 1)
        # 바로 없애니까 아예 초기화가 되어버림
        arr[ci][cj] = 0
        row[ci][k-1] = col[cj][k-1] = square[bIdx][k-1] = 0
        choice[cnt] = 0



row = [[0] * 9 for _ in range(9)]
col = [[0] * 9 for _ in range(9)]
square = [[0] * 9 for _ in range(9)]

arr = []
for i in range(9):
    inp = list(map(int, input()))
    arr.append(inp)
    for j, num in enumerate(inp):
        if num:
            row[i][num-1] = 1
            col[j][num-1] = 1
            idx = board_num(i, j)
            square[idx][num-1] = 1

target = []
lenT = 0
for ii in range(9):
    for jj in range(9):
        if not arr[ii][jj]:
            target.append((ii, jj))
            lenT += 1
choice = [None] * lenT
res_ls = []
backtrack(0)


for x in range(lenT):
    si, sj = target[x]
    arr[si][sj] = res_ls[x]

for elem in arr:
    print(''.join(map(str, elem)))

