import sys

sys.stdin = open('input.txt')

# 1, 2를 빼뜨려서 틀렸었음

def backtrack(idx, before, cost):  # idx: 몇번째로 이동하는 지, before: 이 전 집의 번호
    global mmin
    if cost > mmin: return
    if idx == n:  # n개를 다 고른 경우 -> 이 때 마지막에서 1로 가는 것 구해주기
        if not adj[before - 1][0]: return  # 1로 가는 경로가 없는 경우 -- 1.
        # print(visited, before, cost+adj[before-1][0])
        if mmin > cost+adj[before-1][0]:
            mmin = cost+adj[before-1][0]
            # print(visited, mmin)
        return
    for i in range(2, n+1): # 1이 아닌 경로 고르기
        if i in visited: continue  # 없는 것만
        if not adj[before-1][i-1]:continue # 다음 번호로 가는 경로가 없는 경우 -- 2. 
        visited[idx] = i
        backtrack(idx+1, i, cost+adj[before-1][i-1])
        visited[idx] = 0


n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n
# visited[0] = 1
mmin = int(1e9)
backtrack(1, 1, 0)
print(mmin)