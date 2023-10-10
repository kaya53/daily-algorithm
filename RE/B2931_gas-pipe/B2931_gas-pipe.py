import sys

sys.stdin = open('input.txt')

from collections import deque


def get_block(i, j, dir_ls):

    if dir_ls == [1, 0, 1, 0]: return i+1, j+1, '|'
    elif dir_ls == [0, 1, 0, 1]: return i+1, j+1, '-'
    elif dir_ls == [1, 1, 1, 1]: return i+1, j+1, '+'
    elif dir_ls == [0, 1, 1, 0]: return i+1, j+1, 1
    elif dir_ls == [1, 1, 0, 0]: return i+1, j+1, 2
    elif dir_ls == [1, 0, 0, 1]: return i+1, j+1, 3
    elif dir_ls == [0, 0, 1, 1]: return i+1, j+1, 4


def solution():
    r, c = map(int, input().split())
    arr = [list(input()) for _ in range(r)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    pipes = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
    si, sj, ei, ej = -1, -1, -1, -1
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.': continue
            if arr[i][j] == 'M':
                si, sj = i, j
            elif arr[i][j] == 'Z':
                ei, ej = i, j
            else:
                if arr[i][j] == '|': pipes[i][j] = [1, 0, 1, 0]
                elif arr[i][j] == '-': pipes[i][j] = [0, 1, 0, 1]
                elif arr[i][j] == '+': pipes[i][j] = [1, 1, 1, 1]
                elif arr[i][j] == 1: pipes[i][j] = [0, 1, 1, 0]
                elif arr[i][j] == 2: pipes[i][j] = [1, 1, 0, 0]
                elif arr[i][j] == 3: pipes[i][j] = [1, 0, 0, 1]
                elif arr[i][j] == 4: pipes[i][j] = [0, 0, 1, 1]

    q = deque([(si, sj)])
    visited = [[[0, 0, 0, 0] for _ in range(c)] for _ in range(r)]
    visited[si][sj] = [1, 1, 1, 1]
    res = []
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (ei, ej):
            return get_block(*res)

        for d in range(4):
            ni, nj = ci + delta[d][0], cj + delta[d][1]
            if ni < 0 or ni >= r or nj < 0 or nj >= c: continue
            if arr[ni][nj] != '.':
                if not visited[ni][nj][d] and not visited[ni][nj][(d+2)%4]:
                    q.append((ni, nj))
                    visited[ni][nj][d] = visited[ni][nj][(d+2)%4] = 1
            else:  # 연결해야 할 경우
                # ni, nj가 빈 칸임, d는 뻗어온 방향
                dir_ls = []
                for d2 in range(4):
                    nni, nnj = ni + delta[d2][0], nj + delta[d2][1]
                    if nni < 0 or nni >= r or nnj < 0 or nnj >= c: continue
                    if len(pipes[nni][nnj]) > 1 and pipes[nni][nnj][(d2+2)%4]:
                        dir_ls.append(d2)
                # print(ni, nj, dir_ls)
                if dir_ls:
                    arr[ni][nj] = [0, 0, 0, 0]
                    arr[ni][nj][d] = 1
                    visited[ni][nj][d] = 1
                    for nd in dir_ls:
                        arr[ni][nj][nd] = 1
                        visited[ni][nj][nd] = 1
                    q.append((ni, nj))
                    res = [ni, nj, arr[ni][nj]]

# for _ in range(3):
print(*solution())



