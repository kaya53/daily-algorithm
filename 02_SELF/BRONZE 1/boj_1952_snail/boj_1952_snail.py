import sys

# sys.stdin = open('input.txt')

M, N = map(int, input().split())
arr = [[0] * N for _ in range(M)]

# 오 아래 왼 위 순서
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

now_dir = cnt = ci = cj = 0
arr[ci][cj] = 1
visited = 1
while True:
    # 종료 조건 ; 모든 점을 방문했을 때
    if visited == M*N:
        break
    ni = ci + di[now_dir]
    nj = cj + dj[now_dir]
    
    # 다음 칸이 인덱스 밖이거나 이미 지나간 경우; 방향 전환
    if (ni < 0 or ni >= M or ni < 0 or nj >= N ) or arr[ni][nj] == 1:
        now_dir = (now_dir + 1) % 4
        cnt += 1
    else:
        ci, cj = ni, nj  # 이동
        arr[ci][cj] = 1  # 방문 표시
        visited += 1

print(cnt)