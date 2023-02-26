import sys

sys.stdin = open('sample_input.txt')


def check(i, j):
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
        arr[ni][nj] ^= 1

def choose(idx, ssum):
    if idx == lenP:
        return

    ci, cj = processor[idx][0], processor[idx][1]
    direction = check(ci, cj)
    for k in range(4):
        # 이번 방향으로 갈 수 없으면 건너뛰기
        if not direction[k]: continue 
        connect(ci, cj, k)  # 연결하기
        choose(idx + 1, ssum + direction[k])
        connect(ci, cj, k)  # 연결 해제하기
    choose(idx+1, ssum)

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mmin = int(1e9)
    processor = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if arr[i][j]:
                processor.append((i, j))
    lenP = len(processor)
    choice = [0] * lenP
    choose(0, 0)
    print(f'#{tc} {mmin}')