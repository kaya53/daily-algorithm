from collections import deque
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def direction(s):
    if s == '|': return [1, 3]
    elif s == '-': return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z': return [0, 1, 2, 3]
    elif s == '1': return [0, 1]
    elif s == '2': return [0, 3]
    elif s == '3': return [2, 3]
    elif s == '4': return [1, 2]


def bfs(i, j, dir_ls):
    global ri, rj

    q = deque()
    q.append((i, j, dir_ls))
    visited[i][j] = 1
    
    while q:
        ci, cj, curr_ls = q.popleft()
        for d in curr_ls:  # 갈 수 있는 방향으로만 간다
            ni = ci + dx[d]
            nj = cj + dy[d]
            if ni < 0 or ni >= m or nj < 0 or nj >= n or visited[ni][nj]: continue
            if a[ni][nj] != '.':
                visited[ni][nj] = 1
                nd = direction(a[ni][nj])
                q.append((ni, nj, nd))
            else:  # 빈칸 채워줘야 함
                if a[ci][cj] == 'M' or a[ci][cj] == 'Z': continue
                if not ri and not rj:  # 아직 빈칸 채우지 않은 상태
                    ri, rj = ni + 1, nj + 1  # 답의 범위가 1 ~ n까지 이므로
                nd = (d+2) % 4
                if nd not in check_list:
                    check_list.append(nd)


m, n = map(int, input().split())
visited = [[0] * n for _ in range(m)]

a = []
si = sj = ei = ej = 0
for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j in range(n):
        if row[j] == 'M':
            si, sj = i, j
        elif row[j] == 'Z':
            ei, ej = i, j

check_list, ri, rj = [], 0, 0
bfs(si, sj, [0, 1, 2, 3])
bfs(ei, ej, [0, 1, 2, 3])

for i in range(m):
    for j in range(n):
        if a[i][j] != '.' and not visited[i][j]:
            bfs(i, j, direction(a[i][j]))
check_list.sort()

if len(check_list) == 4:
    print(ri, rj, '+')
else:
    block_list = ['|', '-', '1', '2', '3', '4']
    for s in block_list:
        if check_list == direction(s):
            print(ri, rj, s)