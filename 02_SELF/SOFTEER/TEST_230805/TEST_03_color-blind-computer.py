from collections import deque


def bfs(ssame, si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj]: continue
            if arr[ni][nj] not in ssame: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
    return True


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]

# 이렇게 나눈 이유
# (1)대상이 RGB로 3개뿐
# (2) 어차피 BR이나 RB이나 같은 결과가 나올 것
# (3)여러가지가 가능하면 사전 순으로 빠른 것을 출력하라고 문제 조건에 나왔기 때문에
# 연산할 필요없이 이렇게만 둬도 된다고 판단함
same_ls = [('B', 'R'), ('B', 'G'), ('G', 'R')]

mmax = 0
for same in same_ls:
    visited = [[0] * M for _ in range(N)]
    cnt = 1
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if arr[i][j] in same:
                    cnt += bfs(same, i, j)
                else:
                    cnt += bfs([arr[i][j]], i, j)
    if mmax < cnt: mmax = cnt
print(mmax)