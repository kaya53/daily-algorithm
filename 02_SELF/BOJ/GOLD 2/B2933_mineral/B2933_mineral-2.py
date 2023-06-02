import sys

sys.stdin = open('input.txt')

from collections import deque


def throw_stick(ci, range_ls):
    for cj in range_ls:
        if arr[ci][cj] == 'x':
            arr[ci][cj] = '.'
            return


def check():
    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'x' and not visited[i][j]:
                cluster, visited = bfs(i, j, visited)
                if cluster: return cluster


def bfs(si, sj, visited):
    q = deque([(si, sj)])
    visited[si][sj] = 1

    # down_max = []
    cluster = []
    # mi, mj = 0, 0
    while q:
        ci, cj = q.popleft()

        # if mi < ci:
        #     mi = ci
        #     down_max = [(ci, cj)]
        # elif mi == ci: down_max.append((ci, cj))
        cluster.append((ci, cj))

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= R or nj < 0 or nj >= C or visited[ni][nj] or arr[ni][nj] == '.': continue
            # 땅에 닿으면
            if ni == R-1: return [], visited
            q.append((ni, nj))
            visited[ni][nj] = 1
    if len(cluster) > 1:
        return cluster, visited
    return [], visited


def gravity(clus_ls):
    # 아랫줄, 윗줄 순서대로 정렬
    clus_ls.sort(key=lambda x: [-x[0], x[1]])
    # 일단 대상 칸을 모두 빈칸으로 만들어주기
    for ci, cj in clus_ls:
        arr[ci][cj] = '.'

    t = 1
    flag = True
    while flag:
        for ci, cj in clus_ls:
            # 땅에 닿았거나, 다음 칸이 빈칸이 아니라 못가는 경우
            if ci+t+1 >= N or arr[ci+t+1][cj] == 'x':
                flag = False
                break

        else:  # 모든 칸에 대해 다음 칸으로 갈 수 있는 경우
            t += 1

    # 일단 띄어져있으니까 무조건 한 칸은 내려갈 수 있음
    for ci, cj in clus_ls:
        arr[ci+t][cj] = 'x'


# for _ in range(5):
R, C = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]
N = int(input())
throw = list(map(lambda x: R-int(x), input().split()))

for k in range(N):
    height = throw[k]
    if not k % 2: throw_stick(height, range(C))
    else: throw_stick(height, range(C-1, -1, -1))

    c_res = check()
    if c_res:
        gravity(c_res)
for a in arr:
    print(''.join(map(str, a)))