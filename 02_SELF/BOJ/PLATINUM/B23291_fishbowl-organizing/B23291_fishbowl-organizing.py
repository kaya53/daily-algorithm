import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt')


def put_fish():
    min_f = min(arr[-1])
    for jj in range(N):
        if arr[-1][jj] == min_f:
            arr[-1][jj] += 1


def stack_bowl():
    idxJ = 1
    while True:
        stacked = []
        len_f = N
        for j in range(idxJ):
            tmp = []
            for i in range(N-1, -1, -1):
                if not arr[i][j]: break
                tmp.append(arr[i][j])
                len_f -= 1
            stacked.append(tmp)
        if len(stacked[0]) > len_f:
            return len(stacked[0])  # 종료 조건

        lenI = len(stacked)
        lenJ = len(stacked[0])
        for i in range(lenI-1, -1, -1):
            for j in range(lenJ):
                arr[N-2-i][j] = stacked[lenI-1-i][j]
        arr[-1] = arr[-1][idxJ:] + [0] * idxJ
        idxJ = lenJ


def control_fish(start_r):
    move_tmp = [[0]* N for _ in range(N)]
    for i in range(start_r, N):
        for j in range(N):
            if not arr[i][j]: continue
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or not arr[ni][nj]: continue
                if arr[i][j] > arr[ni][nj]:
                    d = (arr[i][j] - arr[ni][nj]) // 5
                    move_tmp[ni][nj] += d
                    move_tmp[i][j] -= d
    for ii in range(start_r, N):
        for jj in range(N):
            arr[ii][jj] += move_tmp[ii][jj]


def straight(start_r):
    straight_tmp = []
    for j in range(N):
        for i in range(N-1, -1, -1):
            if arr[i][j]: straight_tmp.append(arr[i][j])
            else: break
    # 격자에 1자로 놓기
    for i in range(start_r, N-1):
        arr[i] = [0] * N
    arr[-1] = straight_tmp


def stack_bowl_half():
    half_n = N // 2
    for k in range(2):
        half_tmp = []
        for i in range(N-1, N-k-2, -1):
            t = []
            for j in range(half_n - 1, -1, -1):
                if arr[i][j]: t.append(arr[i][j])
                else:break
            else: half_tmp.append(t)

        # 격자에 적용하기
        for ii in range(k, -1, -1):
            for jj in range(half_n):
                arr[N-2-ii-k][jj] = half_tmp[k-ii][jj]
        for kk in range(k+1):
            arr[N-kk-1] = arr[N-kk-1][half_n:] + [0] * half_n
        half_n //= 2


N, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]

# 초반 어항 설정
arr[-1] = list(map(int, input().split()))

cnt = 0
while True:
    cnt += 1
    put_fish()
    max_i = stack_bowl()  # 물고기 수를 조절할 때 볼 행의 크기; 아래에서부터 max_i 칸
    control_fish(N-max_i)  # N-max_i행 ~ N-1행까지
    straight(N-max_i)
    stack_bowl_half()  # 여기서 i 사이즈 리턴해서 control_fish에 넘겨주기
    control_fish(N-4)
    straight(N-4)

    if max(arr[-1]) - min(arr[-1]) <= K:
        print(cnt)
        break

