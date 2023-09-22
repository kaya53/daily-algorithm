import sys

sys.stdin = open('input.txt')


def left(x2, y2): # 기준 건물과의 기울기가 최소인 건물만 볼 수 있음
    mmin = int(1e9)
    cnt = 0
    for x1 in range(i-1, -1, -1):
        y1 = buildings[x1]
        now = (y2-y1)/(x2-x1)
        if mmin > now:
            mmin = now
            cnt += 1
            # print(y1, y2, cnt)
    return cnt


def right(x1, y1):  # 기준 건물과의 기울기가 최대인 건물만 볼 수 있음
    mmax = -int(1e9)
    cnt = 0
    for x2 in range(x1+1, N):
        y2 = buildings[x2]
        now = (y2 - y1) / (x2 - x1)
        if mmax < now:
            mmax = now
            cnt += 1
            # print(y1, y2, cnt)
    return cnt


# for _ in range(5):
N = int(input())
buildings = list(map(int, input().split()))

ans = 0
for i in range(N):
    now_cnt = left(i, buildings[i]) + right(i, buildings[i])
    if ans < now_cnt: ans = now_cnt
print(ans)