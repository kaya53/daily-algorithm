import sys

sys.stdin = open('input.txt')


def solve(row):
    for c in range(1, N):
        if row[c] - row[c-1] != 1: continue
        elif row[c] - row[c-1] > 1: return False
        std = row[c]
        for num in range(1, L+1):
            now = row[c-num]
            if std - now != 1 or visited[c-num] or c-num < 0: return False

        for n in range(1, L+1):
            visited[c+n] = 1
    return True



N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]

zipped = list(map(list, zip(*arr)))

cnt = 0
for i in range(N):
    visited = [0] * N
    rrow = arr[i]
    oppo_rrow = arr[i][::-1]
    first = arr[i][0]
    
    # 이미 길을 갈 수 있는 경우
    if rrow.count(first) == N:
        print('already', i)
        cnt += 1
        continue
    if solve(rrow):
        print(i, rrow)
        # print(visited)
        cnt += 1
    if solve(oppo_rrow):
        print(i, oppo_rrow)
