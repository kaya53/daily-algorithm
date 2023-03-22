import sys

sys.stdin = open('input.txt')


def dfs(i, j, k):  # k -- 파이프 방향
    global cnt
    if i == N - 1 and j == N - 1:  # 도착점에 도달하면 방법의 수 +1
        cnt += 1
    # k -- 0: 가로, 1: 오른쪽 아래, 2: 세로
    if k == 0 or k == 1:
        if j < N - 1 and house[i][j + 1] == 0:  # house 내부 + 다음칸이 벽이 아닌지 확인
            dfs(i, j + 1, 0)
    if k == 0 or k == 1 or k == 2:
        if i < N - 1 and j < N - 1:
            if house[i + 1][j] == 0 and house[i][j + 1] == 0 and house[i + 1][j + 1] == 0:
                dfs(i + 1, j + 1, 1)
    if k == 1 or k == 2:
        if i < N - 1 and house[i + 1][j] == 0:
            dfs(i + 1, j, 2)


N = int(input())  # 집의 크기
house = [list(map(int, input().split())) for _ in range(N)]

# 현재 파이프가 가로, 세로, 대각선인지 파악 --> 어떻게 움직일 수 있는 지가 다름
# (N-1,N-1)까지 이동
# 초반 위치(1,1), (1,2) --> 여기서는 (0,0), (0,1) 가로로

cnt = 0  # 도착점에 도착하는 방법의 수
# (0,1)에서 dfs 돌리기
dfs(0, 1, 0)
print(cnt)
