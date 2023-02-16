import sys

sys.stdin = open('input.txt')


from collections import deque


# def search(i, j, visited, arr):
#     global cnt_nation, tot_pop, day

    # q = deque()
    # q.append((i, j))
    # tot_pop = arr[i][j]
    # cnt_nation = 1
    # united = deque((i, j))
    # visited[i][j] = 1
    # while q:
    #     ci, cj = q.popleft()
    #     for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #         ni, nj = ci + di, cj + dj
    #         if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
    #         minus = abs(arr[ci][cj] - arr[ni][nj])
    #         if visited[ni][nj] != day and l <= minus <= r:
    #             tot_pop += arr[ni][nj]
    #             cnt_nation += 1
    #             visited[ni][nj] = day
    #             united.append((ni, nj))
    #             q.append((ni, nj))
    #
    # # 큐가 끝났다는 것은 한 연합이 끝난 것
    # flag = 0
    # if len(united) > 1:  # 한 칸만 들어가 있는 경우는 인구 이동이 안 일어남
    #     moved = tot_pop // cnt_nation
    #     while united:
    #         ui, uj = united.popleft()
    #         arr[ui][uj] = moved
    #         flag = 1
    # if flag:
    #     day += 1
    #     return True
    # else: return False


# for _ in range(5):
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

tot_pop = cnt_nation = 0

day = 1
while True:
    # 새로 순회할 때마다(날이 바뀔 때마다) 방문 정보 갱신
    visited = [[0] * n for _ in range(n)]
    # 연합 국가들의 인덱스를 모아놓은 배열
    united = deque()
    # flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == day: continue  # 오늘 방문한 곳이면 패스
            # 초기작업
            q = deque()
            q.append((i, j))
            tot_pop = arr[i][j]
            cnt_nation = 1
            united = deque([(i, j)])
            visited[i][j] = 1
            while q:
                ci, cj = q.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = ci + di, cj + dj
                    if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
                    minus = abs(arr[ci][cj] - arr[ni][nj])
                    # 오늘 방문을 안했고, 인구 차가 범위 내 이면
                    if visited[ni][nj] != day and l <= minus <= r:
                        tot_pop += arr[ni][nj]
                        cnt_nation += 1
                        visited[ni][nj] = day
                        united.append((ni, nj))
                        q.append((ni, nj))

            # 큐가 끝났다는 것은 한 연합이 끝난 것
            flag = 0
            if len(united) > 1:  # 한 칸만 들어가 있는 경우는 인구 이동이 안 일어남
                flag = 1  # 연합이 존재하면 flag를 세운다
                moved = tot_pop // cnt_nation
                while united:
                    ui, uj = united.popleft()
                    arr[ui][uj] = moved

    # flag가 세워진 건 연합이 존재한다는 의미
    if flag:
        day += 1
    else:
        break

# day = 1부터 시작했기 때문에 1을 빼준다
print(day-1)
