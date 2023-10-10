# 소요시간 20분 python 44ms
import sys

sys.stdin = open('input.txt')

def solution():
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    down = []
    minI, minJ = r, c
    maxI, maxJ = 0, 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.': continue
            cnt = 0
            for di, dj in delta:
                ni, nj = i+di, j+dj
                if ni < 0 or ni >= r or nj < 0 or nj >= c or arr[ni][nj] == '.': cnt += 1
            if cnt >= 3: down.append((i, j))
            else:
                if minI > i: minI = i
                if minJ > j: minJ = j
                if maxI < i: maxI = i
                if maxJ < j: maxJ = j
    # print(down)
    # print(minI, minJ)
    # print(maxI, maxJ)
    for ai, aj in down:
        arr[ai][aj] = '.'
    for ri in range(minI, maxI+1):
        for rj in range(minJ, maxJ+1):
            print(arr[ri][rj], end='')
        print()

# for _ in range(2):
solution()