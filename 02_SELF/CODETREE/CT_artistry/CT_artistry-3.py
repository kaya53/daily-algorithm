# 230607
# 그룹 찾기 + 인접한 그룹과 몇 개의 변이 닿아 있는 지 구하기

import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(si, sj, num, grp_no):
    q = deque([(si, sj)])
    visited[si][sj] = 1
    adj = {}
    cnt = 1
    now_grp = grp_no
    while q:
        ci, cj = q.popleft()

        for di, dj in delta:
            ni, nj = ci + di, cj + dj

            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if arr[ni][nj] == num:
                q.append((ni, nj))
                visited[ni][nj] = 1
                cnt += 1
            else:
                # other = grp_no
                if not adj.get(now_grp):
                    adj[now_grp] = [arr[ni][nj], 1]
                else:
                    if arr[ni][nj] == adj[now_grp][0]:
                        adj[now_grp][1] += 1
                    else:
                        pass
                # g_arr[ni][nj] = grp_no
                # if adj.get(grp_no): adj[grp_no] += 1
                # else: adj[grp_no] = 1
    # print(adj)
    return adj, cnt


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(2):
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
half = N//2
visited = [[0] * N for _ in range(N)]

adj_group = []
grp_info = []
score = 0
g_arr = [[0] * N for _ in range(N)]
gnum = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            adj_dict, now_cnt = bfs(i, j, arr[i][j], gnum)
            adj_group.append(adj_dict)
            grp_info.append((now_cnt, arr[i][j]))
            gnum += 1
print(adj_group)
print(grp_info)

for no, adj_d in enumerate(adj_group):
    now = 0
    cnt1, num1 = grp_info[no]
    for adj_no, adj_cnt in adj_d.items():
        cnt2, num2 = grp_info[adj_no]
        now = (cnt1 + cnt2) * num1 * num2 * adj_cnt
        # print(now)