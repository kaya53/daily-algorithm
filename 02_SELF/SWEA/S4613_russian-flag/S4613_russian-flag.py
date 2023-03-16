import sys

sys.stdin = open('input.txt')


# 주어진 배열에서 몇개를 바꿔야 하는 지 판별
def check(choice):
    global mmin

    wh, bl, red = choice
    cnt = 0  # 바꿀 칸 개수
    for x in range(wh):
        for j in range(m):
            if arr[x][j] != 'W':
                cnt += 1
    for y in range(wh, wh+bl):
        for j in range(m):
            if arr[y][j] != 'B':
                cnt += 1
    for z in range(wh+bl, n):
        for j in range(m):
            if arr[z][j] != 'R':
                cnt += 1
    if mmin > cnt:
        mmin = cnt


def comb(idx, ssum):
    if idx == 3:
        if ssum == n:
            check(choice)
        return
    for i in range(1, n - 2 + 1):
        if ssum + i > n: continue
        choice[idx] = i
        comb(idx + 1, ssum + i)


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    choice = [0, 0, 0]  # 흰색 - 파랑 - 빨강 순
    mmin = 2501
    comb(0, 0)
    print(f'#{tc} {mmin}')