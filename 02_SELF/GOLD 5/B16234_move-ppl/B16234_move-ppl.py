import sys

sys.stdin = open('input.txt')


from collections import deque


def search(i, j, visited, arr):
    global cnt_nation, tot_pop
    q = deque()
    q.append((i, j))
    tot_pop = arr[i][j]
    cnt_nation = 1
    tmp = []
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            minus = abs(arr[ci][cj] - arr[ni][nj])
            if l <= minus <= r and (not visited[ci][cj] or not visited[ni][nj]):
                if not visited[ci][cj]:
                    visited[ci][cj] = 1
                    cnt_nation += 1
                    tot_pop += arr[ci][cj]
                    tmp.append((ci, cj))
                if not visited[ni][nj]:
                    visited[ni][nj] = 1
                    cnt_nation += 1
                    tot_pop += arr[ni][nj]
                    tmp.append((ni, nj))
                q.append((ni, nj))

    # 큐가 끝났다는 것은 한 연합이 끝난 것
    if cnt_nation:
        moved = tot_pop // cnt_nation
        tmp.append(moved)
        united.append(tmp)
        tot_pop = cnt_nation = 0
        return True
    return False


def move(united):
    global res
    while united:
        info = united.popleft()
        moved = info.pop()
        for ui, uj in info:
            arr[ui][uj] = moved
    res += 1


# for _ in range(5):
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

tot_pop = cnt_nation = 0

res = 0
while True:
    # 새로 순회할 때마다 방문 정보 갱신
    visited = [[0] * n for _ in range(n)]
    united = deque()
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                search(i, j, visited, arr)
    if united:
        move(united)
    else: break
print(res)
