import sys

sys.stdin = open('input.txt')

from collections import deque


def is_connected(si, sj, arr):
    # 여기서 녹이기까지 해주고 녹인 후에 빙하가 남아있으면 cnt+=1 해주기 -- sum 대신
    # 남은 빙하가 없다면 print(0) 해주기
    global conn_cnt

    q = deque()
    q.append((si, sj))
    # 방문 처리, 연결 처리
    arr[si][sj][0] -= arr[si][sj][1]
    arr[si][sj][1] = -1
    if arr[si][sj][0] < 0: arr[si][sj][0] = 0
    conn_cnt += 1
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
            if arr[ni][nj][0] > 0 and arr[ni][nj][1] != -1:  # 빙하가 있고 방문하지 않았으면; 방문 여부를 빙하가 있고, 두번째 요소가 없으면(이미 뺄셈을 해주었다면)
                # 방문했으면 녹이는 부분이 0
                conn_cnt += 1  # 중복 방지; 잘 돌아가는 지 확인용? 아니 얘는 필요할 거 같아
                # 일종의 방문 처리 겸 녹여주기
                arr[ni][nj][0] -= arr[ni][nj][1]
                if arr[ni][nj][0] < 0: arr[ni][nj][0] = 0  # 음수이면 0으로
                arr[ni][nj][1] = -1
                q.append((ni, nj))


# for _ in range(3):
n, m = map(int, input().split())
arr = [[[0, 0] for _ in range(m)] for _ in range(n)]  # 현재 빙하, 녹일 수 있는 숫자, 방문 여부(필요없을 것 같음)
for i in range(n):
    inp = list(map(int, input().split()))
    for j in range(m):
        if inp[j]:
            arr[i][j][0] = inp[j]

year = 0
while True:
    year += 1
    # 1. 이번 연도의 빙하 개수 세기, 빙하 녹이기
    ice_cnt = 0
    # 모서리는 무조건 0으로 둘러져있으니까
    si, sj = 0, 0
    for ci in range(1, n-1):
        for cj in range(1, m-1):
            # if year > 1:
            if arr[ci][cj][0]:
                si, sj = ci, cj
                arr[ci][cj][1] = 0  # 이전 단계의 방문 초기화; 이번에도 방문을 해야하면
                ice_cnt += 1
                # melt_num = 0
                # 얼마나 녹일 수 있는 지 담아놓기
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= m: continue
                    if not arr[ni][nj][0]:  # 주변에 빙하가 있고, 현재 칸이 1이상이면
                        arr[ci][cj][1] += 1

    if not ice_cnt:  # 두 덩이가 안되고 다 녹아버렸으면
        print(0)
        break

    conn_cnt = 0
    is_connected(si, sj, arr)

    if conn_cnt != ice_cnt:
        print(year-1)
        break