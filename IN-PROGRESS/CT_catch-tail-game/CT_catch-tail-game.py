import sys

sys.stdin = open('input.txt')


# 머리, 꼬리, 나머지 팀원들의 방향 구하기
# 큐 써서 다시 짜기
def get_members_dir():
    head = []
    tail = []
    rest = []
    for i in range(N):
        for j in range(N):
            if not arr[i][j]: continue
            visited[i][j] = 1
            d = 0
            ni, nj = i + delta[d][0], j + delta[d][0]
            if (ni < 0 or ni >= N or nj < 0 or nj >= N) or not arr[ni][nj]:
                d = (d+1) % 4
                ni, nj = i + delta[d][0], j + delta[d][0]
            visited[ni][nj] = 1
            if arr[ni][nj] == 1: head = [[ni, nj, d]]
            elif arr[ni][nj] == 3: tail = [[ni, nj, d]]
            elif arr[ni][nj] == 2: rest.append([ni, nj, d])
    return head, tail, rest


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상 순
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 머리, 중간, 꼬리 팀원들의 위치와 방향 구하기
visited = [[0] * N for _ in range(N)]
for _ in range(M):
    print(get_members_dir())