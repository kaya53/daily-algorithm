import sys

# sys.stdin = open('input.txt')

from collections import deque


def move_fireball(infos):
    while infos:
        ci, cj, m, s, d = infos.popleft()
        ni = (ci + dir[d][0] * s) % n
        nj = (cj + dir[d][1] * s) % n
        if m == 0:
            arr[ci][cj] = 0
            continue
        if not arr[ni][nj]:  # 이동한 칸에 파볼이 없으면
            arr[ni][nj] = [m, s, d, 0, 1]  # 질량, 속력, 방향, 방향 플래그, 파볼 개수
        else:  # 있으면
            arr[ni][nj][0] += m
            arr[ni][nj][1] += s
            arr[ni][nj][-1] += 1
            # 방향 체크
            if not arr[ni][nj][3]:  # 방향 플래그 = 0일 때만 체크
                if arr[ni][nj][2] % 2 != d % 2:  # 이전 방향과 현재 방향의 홀짝이 다르면
                    arr[ni][nj][3] = 1
            # 방향 체크 끝났으면 지금 방향으로 갱신해주기
            arr[ni][nj][2] = d


def after_move():
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                if arr[i][j][-1] >= 2:
                    x = arr[i][j]
                    new_m = x[0] // 5
                    new_s = x[1] // x[-1]
                    if new_m:  # 질량이 0이 아닌 경우만
                        for new_d in range(x[3], x[3] + 7, 2):
                            infos.append([i, j, new_m, new_s, new_d])
                    # arr[i][j] = 0  # 나누어졌으면 그 칸은 다시 0
                else:  # 합쳐지지 않은 파볼들도 다음에 이동을 해야하니까 다시 infos에 넣어주기
                    infos.append([i, j] + arr[i][j][:3])  # [m, s, d, 0, 1]
                arr[i][j] = 0


n, m, k = map(int, input().split())
infos = deque([list(map(int, input().split())) for _ in range(m)])
arr = [[0] * n for _ in range(n)]  # 파이어볼 현황판
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for x in range(m):
    infos[x][0] -= 1
    infos[x][1] -= 1


for _ in range(k):  # k번 이동하므로
    # 1. 파이어볼 이동
    move_fireball(infos)
    after_move()

res = 0
for kk in infos:
    res += kk[2]

print(res)

### 틀린 이유
# 1. 방향 체크
    # - 모두 더해준 후 나머지를 보면 1,3 / 2,4 와 같이 짝을 지어서 홀짝이 나오는 경우는 걸러내지 못한다.
# 2. 이동한 파이어볼도 또 다음 턴에서 이동을 시켜야 하는데 안 시킴
    # - 2개 이상이어서 나뉜 파이어볼만 이동 처리 해줌
# 3. 파이어볼 이동 후 초기화 시점
    # - 파이어볼이 이동했다면 초기화를 해줘야 하는데 무조건 0으로 해버리면 다른 파이어볼에도 영향을 줄 수 있음
    # - 그래서 이동 후 2개 이상의 파이어볼이 있는 경우는 4개로 나눠주고 나서 초기화를 시켜주었고
    # - 한 개의 파이어볼이 있는 칸은 다음 이동 큐에 넣고 초기화를 시켜서
    # - 이동 한 턴이 끝나면 arr이 무조건 0이 되도록 했다.