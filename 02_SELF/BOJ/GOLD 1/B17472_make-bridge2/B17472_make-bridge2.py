# 230523 python 88ms => 68ms
# 최소 신장 트리
# 어떻게 최소 신장 트리 문제인 지 생각할 수 있을까?
# 1. 섬을 연결하는 다리 길이의 총합이 최소가 되도록 연결하라고 함
# 2. 모든 섬이 연결되지 않는 경우는 -1 출력

# 크루스칼
# 다리가 수직, 수평만 가능하기 때문에, 가능한 간선이 많지 않을 것이기 때문에 가능하다.

# 최적화
# if ret and ret not in edge_ls: edge_ls.append(ret) 이 부분에서 not in 코드 빼니까 68ms 나옴
import sys

sys.stdin = open('input.txt')

from collections import deque


def find_island(si, sj, marked):
    q = deque([(si, sj)])
    visited_island[si][sj] = 1
    arr[si][sj] = marked

    island_loc = [(si, sj)]
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            # 인덱스 밖, 이미 탐색한 곳, 바다는 제외
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited_island[ni][nj] or not arr[ni][nj]: continue
            q.append((ni, nj))
            visited_island[ni][nj] = 1
            arr[ni][nj] = marked
            island_loc.append((ni, nj))
    return island_loc


def find_bridge(island_no, si, sj, d):
    q = deque([(si, sj, 0)])
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1

    edge = ()
    while q:
        ci, cj, length = q.popleft()

        ni, nj = ci + delta[d][0], cj + delta[d][1]
        # 인덱스 밖, 땅인 곳 제외
        if ni < 0 or ni >= N or nj < 0 or nj >= M or arr[ni][nj] == island_no or visited[ni][nj]: continue
        # 양방향이니까 나보다 번호가 큰 섬이랑만 보면 됨
        if 0 < arr[ni][nj] < island_no: continue
        
        # 어떤 섬에 도달함
        if arr[ni][nj] > island_no:
            if length > 1: edge = (island_no, arr[ni][nj], length)
        # 바다
        elif arr[ni][nj] == 0:
            q.append((ni, nj, length+1))
            visited[ni][nj] = 1

    if edge: return edge


def find(a):
    if parents[a] < 0: return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_b == root_a: return False
    # parents[root_a] += parents[root_b]
    parents[root_b] = root_a
    return True


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(4):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1. 섬 찾기
visited_island = [[0] * M for _ in range(N)]
num = 1
whole_island = []
for i in range(N):
    for j in range(M):
        if arr[i][j] and not visited_island[i][j]:
            whole_island.append(find_island(i, j, num))
            num += 1

# 2. 섬과 섬 간의 간선 찾기
edge_ls = []
for idx, island in enumerate(whole_island, start=1):
    for bi, bj in island:
        for k in range(4):  # 다리가 중간에 방향이 바뀌면 안되니까
            ret = find_bridge(idx, bi, bj, k)
            # if ret and ret not in edge_ls: edge_ls.append(ret)
            if ret: edge_ls.append(ret)

# 3. 가중치를 기준으로 정렬
edge_ls.sort(key=lambda x: x[-1])


# 4. 각 섬을 노드로 해서 union find를 한다.
parents = [-1] * (num - 1)
res = 0
for s, e, edge_len in edge_ls:
    if union(s-1, e-1): res += edge_len

# output
# 이렇게 안하고 연결된 간선의 개수가 (정점-1)개 이면으로 해도 됨
tmp = 0
for p in parents:
    if p < 0: tmp += 1
    
# 연결된 섬 덩어리가 1개 이상 => 모든 섬이 연결된 것이 아님
if tmp > 1: print(-1)
else: print(res)