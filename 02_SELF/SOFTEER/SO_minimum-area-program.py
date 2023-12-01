# bfs보다 dfs가 나은 이유
# 1. bfs를 사용해서 모든 격자를 다보면 그 안에서 최소 면적을 찾기가 힘듬
# 2. 색상을 모두 포함해야 하므로, "색을 기준으로 두고 탐색"하는 것이 낫다
# - 색은 최대 20개이므로, dfs를 해도 depth가 20이라 양호
# - 각 dfs 단계마다 왼쪽 모서리 점, 오른쪽 모서리 점을 갱신해나가면 된다

def dfs(idx, minI, minJ, maxI, maxJ):
    global mmin

    if idx == K:  # 모든 색 다 봄
        w = maxJ - minJ
        h = maxI - minI
        tot = w * h
        if mmin > tot: mmin = tot
        return

    for ni, nj in colors[idx]:
        # colors[idx]가 여러 개일 때 기존 값이 바뀌면 안되니까 'n_'을 붙임
        # minI, minJ : 가장 왼쪽 모서리
        # maxI, maxJ: 가장 오른쪽 모서리
        n_minI = min(minI, ni)
        n_minJ = min(minJ, nj)
        n_maxI = max(maxI, ni)
        n_maxJ = max(maxJ, nj)

        now = (n_maxI - n_minI) * (n_maxJ - n_minJ)
        if mmin > now:  # 가지치기 - 이거 안넣으면 시초될 수도 
            dfs(idx + 1, n_minI, n_minJ, n_maxI, n_maxJ)


N, K = map(int, input().split())
colors = [[] for _ in range(K)]
for k in range(N):
    a, b, c = map(int, input().split())
    colors[c - 1].append((a, b))

mmin = int(1e9)
for i, j in colors[0]:
    dfs(0, 1001, 1001, -1001, -1001)
print(mmin)
