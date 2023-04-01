import sys
from collections import deque

input = sys.stdin.readline


def throw_stick(direc, row):
    for j in direc:
        if arr[row][j] == 'x':
            arr[row][j] = '.'
            return


# 중력 적용되는 클러스터만 찾기
def find_cluster():
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '.' or visited[i][j]: continue
            clus_ls, visited = bfs(i, j, visited)
            if clus_ls:
                return clus_ls


def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    tmp = [(i, j)]
    flag = True
    while q:
        ci, cj = q.popleft()
        if ci == N-1: # 중력을 적용할 클러스터가 아님
            flag = False
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
            if visited[ni][nj] or arr[ni][nj] == '.': continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            tmp.append((ni, nj))
    # 마지막에 리턴할 때 중력 적용을 할 필요가 있는 애랑 없는 애를 나눴어야 했는데
    # 39번째 줄에서 리턴을 해버리는 바람에 틀렸었음
    if flag: return tmp, visited
    else: return [], visited


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


# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(N)]

K = int(input())
throw = list(map(int, input().split()))
for kk in range(K):
    if not kk % 2:
        throw_stick(range(M), N - throw[kk])
    else:
        throw_stick(range(M-1, -1, -1), N - throw[kk])

    cluster = find_cluster()
    if cluster: gravity(cluster)

for a in arr:
    print(''.join(map(str, a)))

