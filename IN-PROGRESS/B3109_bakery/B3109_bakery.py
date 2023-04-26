# 가능한 위로 붙여서 하는 것이 최선
# 그리디: 내 판단이 중요할 수 있음 => 이 문제의 경우는 어떤 방향으로 먼저 파이프를 놓을 지가 중요함
# 먼저 놓는 파이프가 중요

# bfs를 쓰면 안되는 이유:
# 한 파이프를 놓으면 그 자리에 파이프를 놓을 수 없기 때문에 visited를 사용해야 하는데 
# 하나의 라인을 동시에 놓으면서 갈 수 없으니까 dfs를 사용해야 함
import sys

sys.stdin = open('input.txt')


def dfs(si, sj):
    if sj == M-1:
        return 1
    for di in [-1, 0, 1]:
        ni, nj = si + di, sj + 1
        # 인덱스 밖
        if ni < 0 or ni >= N or nj < 0 or nj >= M: continue
        # 건물이 있거나 이미 방문한 곳
        if arr[ni][nj] == 'x' or visited[ni][nj]: continue
        # 방문 처리
        visited[ni][nj] = 1
        # 리턴 1이 된 건 파이프라인이 연결된거니까 계속 리턴 1 해주기
        if dfs(ni, nj): return 1
    return 0


# for _ in range(2):
N, M = map(int, input().split())
arr = [input() for _ in range(N)]

cnt = 0
visited = [[0] * M for _ in range(N)]
for i in range(N):
    if visited[i][0]: continue  # 연결된 칸은 더 이상 가지 않음
    cnt += dfs(i, 0)

print(cnt)
