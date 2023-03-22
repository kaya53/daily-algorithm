import sys

sys.stdin = open('input.txt')

from collections import deque

def spread(choice, arr, zeros):
    global mmin
    now_max = 0
    # 활성 바이러스 놓기
    q = deque()
    for vi, vj in choice:
        arr[vi][vj] = -3
        q.append((vi, vj, 0))
    while q:
        ci, cj, time = q.popleft()  # 바이러스가 퍼진 점
        # time과 now_max를 비교하면 비활성에서 활성으로 된 바이러스가 퍼져나갈 경우에
        # 시간이 한 번 더 세지게 된다
        if now_max < arr[ci][cj]:
            now_max = arr[ci][cj]
        # if time >= mmin:  # 최소 시간 이상이면 더 이상 보지 말기
            # return
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            # 건너뛰기
            # 1. 인덱스 밖
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            # 2. 벽, 이미 지나간 경우, 활성 바이러스의 경우
            if arr[ni][nj] == -1 or arr[ni][nj] > 0 or arr[ni][nj] == -3: continue
            q.append((ni, nj, time + 1))
            # 비활성 -> 활성
            if arr[ni][nj] == -2:
                arr[ni][nj] = -3
            # 빈 칸에 퍼뜨리기
            if not arr[ni][nj]:
                zeros -= 1
                arr[ni][nj] = time + 1
    
    # 빈칸이 있으면 최소값 갱신하지 말고 패스
    if zeros: return
    if mmin > now_max:
        mmin = now_max


def activate(idx, si):
    if idx == m:  # 활성시킬 바이러스를 다 고름
        spread(choice, [ls[:] for ls in arr], zero_cnt)
        return

    for i in range(si, len(virus)):
        choice[idx] = virus[i]
        activate(idx+1, i+1)
        choice[idx] = 0


# for _ in range(12):
n, m = map(int, input().split())  # 격자 크기, 놓을 수 있는 활성 바이러스 개수
arr = [list(map(int, input().split())) for _ in range(n)]
mmin = int(1e9)
zero_cnt = n*n

# 전체 비활성 바이러스 세기
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:  # 모든 바이러스
            virus.append((i, j))
            arr[i][j] = -2  # 비활성 바이러스
            zero_cnt -= 1
        # 벽은 -1로 만들어주기
        if arr[i][j] == 1:
            arr[i][j] = -1
            zero_cnt -= 1

if zero_cnt:  # 이걸 안 해줘서 처음에 시간 초과 남
    choice = [0] * m
    activate(0, 0)
    if mmin == int(1e9):
        print(-1)
    else:
        print(mmin)
else:  # 처음부터 빈칸이 없으면 연산 안하기
    print(0)