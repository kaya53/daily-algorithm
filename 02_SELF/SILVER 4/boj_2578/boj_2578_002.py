# ๐ก bingo ํจ์ ์์ cnt์ namespace์ ๋ํด ๋ค์ ์๊ฐํด๋ณด๊ธฐ ๐ก

import sys

sys.stdin = open('input.txt')


bingo_arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(5)]


def find_idx(num):
    for i in range(5):
        for j in range(5):
            if num == bingo_arr[i][j]:
                return i, j


def bingo(row, col):
    global ssame, ssum, cnt
    if row == col:
        ssame += col
        if ssame == 15: cnt += 1
    if row + col == 6:
        ssum += col
        if ssum == 15: cnt += 1
    rows[row-1] += col
    cols[col-1] += col
    if rows[row-1] == 15: cnt += 1
    if cols[col-1] == col*5: cnt += 1

    return cnt


# mc๊ฐ ๋ถ๋ฌ์ค ์ซ์๋ ํ ์ค์ฉ ๋ฐ์ ์ํํ๋ฉฐ ์ธ๋ฑ์ค๋ฅผ ์ฐพ๋๋ค
res = 0
rows = [0] * 5
cols = [0] * 5
ssum = 0
ssame = 0
cnt = 0
for _ in range(5):
    mc_num = list(map(int, sys.stdin.readline().rstrip().split()))
    for num in mc_num:
        res += 1
        row, col = find_idx(num)
        bingo(row+1, col+1)
        if cnt >= 3:
            break
    if cnt >= 3:
        print(res)
        break


