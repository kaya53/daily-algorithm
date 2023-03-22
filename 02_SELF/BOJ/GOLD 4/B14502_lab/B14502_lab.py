import sys

sys.stdin = open('input.txt')

## 이주 코드보고 배운 점
# deepcopy(copy_arr = [elem[:] for elem in arr)를 쓰지 않고
# visited 배열을 따로 마련해서 원래 배열은 바꾸지 않는 게 시간이 훨씬 덜 걸린다


# def dfs(si, sj, copy_arr):
#     global now_safe
#
#     if not arr[si][sj]:
#         copy_arr[si][sj] = 2  # 감염 처리
#         now_safe -= 1  # 안전 구역 감소
#
#     # 재귀 유도
#     for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#         ni, nj = si + di, sj + dj
#         if ni < 0 or ni >= N or nj < 0 or nj >= M: continue  # 인덱스 밖이면
#         if not copy_arr[ni][nj]:  # 감염될 수 있는 애들만 다음 재귀로 넘기기
#             dfs(ni, nj, copy_arr)
#     # 4방향이 막힌 경우
#     return

from collections import deque

def bfs(visited):
    global now_safe

    q = deque(virus_init)
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            # 인덱스 밖 or 방문한 적이 있음 or 벽
            if ni < 0 or ni >= N or nj < 0 or nj >= M or visited[ni][nj] or arr[ni][nj]: continue
            visited[ni][nj] = 1
            now_safe -= 1
            q.append((ni, nj))
    return now_safe


def comb(cnt, arr):
    global mmax, now_safe

    if cnt == 3:
        # 여기서 dfs 돌리기
        # 각 조합마다 safe 갱신 - now_safe는 전역에서 관리
        now_safe = init_safe
        visited = [[0] * M for _ in range(N)]
        now_safe = bfs(visited)
        if mmax < now_safe:
            mmax = now_safe
        return
    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                arr[i][j] = 3  # 새로 생긴 벽임을 표시하기 위해; 나중에 바꾸자
                comb(cnt+1, arr)
                arr[i][j] = 0

# for _ in range(3):
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus_init = []
init_safe = N*M - 3 # 안전 영역 크기; 0의 개수, 3개는 무조건 뽑으니까 일단 빼고 시작
now_safe = 0
mmax = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus_init.append((i, j))
            init_safe -= 1
        elif arr[i][j] == 1:
            init_safe -= 1
# print(safe)
comb(0, arr)  # 벽 세울 곳 구하기
print(mmax)