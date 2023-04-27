# 가능한 위로 붙여서 하는 것이 최선
# 그리디: 내 판단이 중요할 수 있음 => 이 문제의 경우는 어떤 방향으로 먼저 파이프를 놓을 지가 중요함
# 먼저 놓는 파이프가 중요

# bfs를 쓰면 안되는 이유:
# 한 파이프를 놓으면 그 자리에 파이프를 놓을 수 없기 때문에 visited를 사용해야 하는데 
# 하나의 라인을 동시에 놓으면서 갈 수 없으니까 dfs를 사용해야 함

# 실패한 파이프에 대한 방문 표시도 되돌리지 않음
# => 최선의 선택으로 했던 시도가 불가능했다면 차선으로 시도해도 불가능하기 때문에

# 뒤에 오는 애한테 영향을 주는가 안주는가
# dfs: 하나의 답을 향해서 직진

# bfs: 가능한 답을 모두 하면서 가봄; 최단은 유리하지만 하나의 답을 찾아야하는 상황에서는 불리
# bfs로 퍼뜨릴 때 가능한 상황이 모두 마킹되기 때문에 그 마킹이 다음 애가 답을 찾는 과정까지 방해하면 bfs가 적절치 않음

import sys

sys.stdin = open('input.txt')


def dfs(si, sj):
    # M-2로 해도 됨 => 마지막 열은 무조건 비어 있으니까 M-2에 도착했으면 무조건 파이프 놓기에 성공한 것임
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
    cnt += dfs(i, 0)

print(cnt)
