import sys

sys.stdin = open('sample_input.txt')


def check(i, j):  # 이 프로세서가 뻗을 수 있는 방향을 체크
    direction = [0, 0, 0, 0]  # 4방향에 얼마나 연결할 수 있는지
    for k in range(4):
        ni, nj = i, j
        lenD = 0
        while 0 < ni < n-1 and 0 < nj < n-1:
            lenD += 1
            ni += dir[k][0]
            nj += dir[k][1]
            if arr[ni][nj]: break
        else:  # break없이 인덱스 밖이어서 빠져나온 경우
            direction[k] = lenD
    return direction


def connect(si, sj, k):  # 선을 연결하거나 해제
    ni, nj = si, sj
    while 0 < ni < n-1 and 0 < nj < n-1:
        ni += dir[k][0]
        nj += dir[k][1]
        arr[ni][nj] ^= 1  ## 중요!! ##


def choose(idx, ssum, connected):
    global mmin

    if idx == lenP:
        # print(ssum)
        # 연결된 코어가 최대일때, 전선의 길이의 합
        # 연결된 코어가 최대인 경우가 여러 개이면, 전선이 최소
        if mmin[0] < connected:
            mmin[0] = connected
            mmin[1] = ssum
        elif mmin[0] == connected and mmin[1] > ssum:
            mmin[1] = ssum
        return

    ci, cj = processor[idx][0], processor[idx][1]  # 프로세서 하나를 고른다.
    direction = check(ci, cj)  # 이 프로세서에서 갈 수 있는 방향을 파악한다.
    for k in range(4):
        # 이번 방향으로 갈 수 없으면 건너뛰기
        if not direction[k]: continue 
        connect(ci, cj, k)  # 연결하기
        choose(idx + 1, ssum + direction[k], connected+1)  # 그 다음 프로세서를 선택하러 간다.
        connect(ci, cj, k)  # 연결 해제하기
    choose(idx+1, ssum, connected)  # 아무 연결도 안될 때, 프로세서를 선택하러 간다.


dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mmin = [0, int(1e9)]
    processor = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j]:
                processor.append((i, j))
    lenP = len(processor)
    choice = [0] * lenP
    choose(0, 0, 0)
    print(f'#{tc} {mmin[1]}')