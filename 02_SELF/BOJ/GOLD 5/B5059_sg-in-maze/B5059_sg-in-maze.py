# 메모리 초과 발생
# - 완탐 돌리면 메초 남

# dp 사용
# 유의할 점
# 1. dp 테이블
# - 이전 턴에 방문했던 칸도 다시 방문할 수 있기 때문에 turn마다 다르게 경로의 수를 세줘야 한다
# => 그렇기 때문에 3차원 배열이 필요하다
# 1-1) 테이블의 크기
# - N번 이동을 하는 것이므로 좌우 이동을 고려해서 2*N + 1 크기로 만들고
# - 정가운데서 이동을 시작해야 한다
# - N번 이동이 가능하므로 가장 바깥쪽 3차원의 크기는 N+1로 해야 한다
# 2. 육각형
# - 인접이 6군데라는 것이기에 인접을 잘 봐야 한다
# - 열을 중심으로 좌표를 매기고, 홀수 열일때, 짝수 열일 때 구분해서 인접을 찾으면 된다
# 3. 시작점
# - 미로는 무한으로 뻗어나갈 수 있기에 처음부터 6개 방향 모두 다 갈 수 있다
# - 즉, board를 만들고 그 중심에서 시작해야 한다
# 4. 점화식
# - t번째 턴에서 (N, N)에서 출발해 (ci, cj)까지 올 수 있는 경우의 수
# = t-1번째 턴에서 (N, N)에서 출발해 (ci, cj)의 인접 칸까지 올 수 있는 경우의 수를 모두 더한 것
import sys

sys.stdin = open('input.txt')


def solution(N):
    # N번까지 이동 가능하니까
    dp = [[[0] * maxN for _ in range(maxN)] for _ in range(N+1)]
    dp[0][N][N] = 1
    for t in range(1, N+1): # 14
        for ci in range(maxN):  # 29
            for cj in range(maxN):  # 29
                delta = deltas[0]  # 짝수
                if cj % 2: delta = deltas[1]
                for di, dj in delta:
                    ni, nj = ci+di, cj + dj
                    if ni < 0 or ni >= maxN or nj < 0 or nj >= maxN: continue
                    dp[t][ci][cj] += dp[t-1][ni][nj]
        # print('turn ---------', t, '------------')
        # for d in dp[t]:
        #     print(d)
        # print()
    return dp[N][N][N]


deltas = [
    [(-1, 0), (-1, 1), (0, 1), (1, 0), (0, -1), (-1, -1)],
    [(-1, 0), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
]
T = int(input())
for _ in range(T):
    N = int(input())
    maxN = 2*N + 1
    print(solution(N))