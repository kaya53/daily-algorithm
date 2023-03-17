import sys
from collections import deque

# sys.stdin = open('input.txt')

input = sys.stdin.readline

def rolling_dice(d, si, sj):
    ni, nj = si + delta[d][0], sj + delta[d][1]
    if ni < 0 or ni >= n or nj < 0 or nj >= m:
        d = (d+2) % 4
        ni, nj = si + delta[d][0], sj + delta[d][1]

    if d == 0:  # 북
        northsouth.append(northsouth.popleft())
        eastwest[1] = northsouth[1]
    elif d == 1:  # 동
        eastwest.appendleft(eastwest.pop())
        eastwest[0], northsouth[-1] = northsouth[-1], eastwest[0]
        northsouth[1] = eastwest[1]
    elif d == 2:  # 남
        northsouth.appendleft(northsouth.pop())
        eastwest[1] = northsouth[1]
    elif d == 3:  # 서
        eastwest.append(eastwest.popleft())
        eastwest[-1], northsouth[-1] = northsouth[-1], eastwest[-1]
        northsouth[1] = eastwest[1]

    return d, ni, nj, 7-eastwest[1]


def calc_score(arrive_num, ei, ej):
    q = deque()
    q.append((ei, ej))
    visited = [[0] * m for _ in range(n)]
    visited[si][sj] = 1
    ff_cnt = 1  # 덩어리 개수
    while q:
        ci, cj = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj]: continue
            if arr[ni][nj] != arrive_num: continue
            q.append((ni, nj))
            visited[ni][nj] = 1
            ff_cnt += 1

    return ff_cnt * arrive_num


def get_dir(d, bottom, arrive_num):
    if bottom > arrive_num:
        return (d+1) % 4
    elif bottom < arrive_num:
        return (d-1) % 4
    else:
        return d


# for _ in range(8):
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
eastwest = deque([4, 1, 3])  # 가장 위, 주사위 기준 왼쪽 -> 오른쪽
northsouth = deque([2, 1, 5, 6])  # 가장 위, 주사위 기준 위쪽 -> 아래쪽
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 초기값
d, si, sj = 1, 0, 0
score = 0
for _ in range(k):
    d, si, sj, bottom = rolling_dice(d, si, sj)
    score += calc_score(arr[si][sj], si, sj)  # 여기 si, sj는 주사위 굴린 이후의 좌표
    d = get_dir(d, bottom, arr[si][sj])

print(score)