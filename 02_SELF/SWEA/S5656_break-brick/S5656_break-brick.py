import sys
from collections import deque

sys.stdin = open('sample_input.txt')


def down_brick(arr):
    for col in range(c):
        stack = deque()
        for i in range(r):
            if arr[i][col]:
                stack.append(arr[i][col])
                arr[i][col] = 0
        row = r-1
        while stack:
            arr[row][col] = stack.pop()
            row -= 1
    return arr


def break_brick(choice, arr):
    global flag

    cnt = 0
    for col in choice:
        si, sj = 0, col

        while arr[si][sj] == 0:
            if si == r-1: break
            si += 1

        q = deque()
        q.append((si, sj, arr[si][sj]))
        while q:
            ci, cj, size = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                for k in range(size):
                    ni, nj = ci + di*k, cj + dj*k
                    if ni < 0 or ni >= r or nj < 0 or nj >= c: break
                    if not arr[ni][nj]: continue
                    if arr[ni][nj] > 1 and k:
                        q.append((ni, nj, arr[ni][nj]))
                    arr[ni][nj] = 0  # 깨기
                    cnt += 1
        if cnt == whole_cnt:
            flag = True
            return cnt
        arr = down_brick(arr)
    return cnt


def backtrack(idx):
    global mmax
    if flag: return
    if idx == n:
        now_cnt = break_brick(choice, [x[:] for x in arr])
        if now_cnt and mmax < now_cnt:
            mmax = now_cnt
        return
    for nc in range(c):
        choice[idx] = nc
        backtrack(idx+1)
        choice[idx] = 0


t = int(input())
for tc in range(1, t+1):
    n, c, r = map(int, input().split())
    arr = []
    whole_cnt = 0
    for _ in range(r):
        inp = list(map(int, input().split()))
        arr.append(inp)
        whole_cnt += (c - inp.count(0))

    mmax = 0
    choice = [0]*n
    # 이미 다 깨졌으면 더 이상 볼 필요가 없도록 => 이게 최대로 깨진거니까
    flag = False
    backtrack(0)
    print(f'#{tc} {whole_cnt - mmax}')