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
                res = bfs(i, j, visited)
                if res[0] is True:
                    # print(res[1], res[2], sep='\n')
                    # print()
                    return res[1]
                else: visited = res[1]


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
            if ni == R-1: return False, visited
            q.append((ni, nj))
            visited[ni][nj] = 1
    if len(cluster) > 1:
        return True, sorted(cluster, reverse=True)
    return False, visited


def gravity(cluster):
    # 몇 칸 내려갈 수 있는 지 세기
    new = cluster[:]
    down = 1
    flag = False
    # for a in arr:
    #     print(a)
    # print()
    # print(new)
    while True:
        for i in range(len(cluster)):
            ci, cj = new[i]
            if ci + down == R-1 or (arr[ci+down][cj] == 'x' and (ci+down, cj) not in cluster):
                flag = True
                break
            new[i] = (ci+down, cj)
        else: down += 1
        if flag: break
    for i in range(len(cluster)):
        ci, cj = cluster[i]
        ni, nj = new[i]
        arr[ni+1][nj] = 'x'
        arr[ci][cj] = '.'


for _ in range(3):
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