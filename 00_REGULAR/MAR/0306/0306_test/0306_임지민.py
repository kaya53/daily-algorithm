# 1번
if True:
    from collections import deque

    n, m = map(int, input().split())  # 행, 열의 길이; 1, 1부터 시작
    r, c, s, k = map(int, input().split())  # 말의 위치, 졸의 위치
    board = [[0] * m for _ in range(n)]  # 장기판

    dir_ls = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]
    # 말에서 시작해 bfs
    res = 0
    q = deque()
    q.append((r - 1, c - 1, 0))  # 말의 시작 위치, 이동 횟수
    while q:
        mi, mj, move_cnt = q.popleft()
        if mi == s - 1 and mj == k - 1:
            res = move_cnt
            break

        for di, dj in dir_ls:
            ni, nj = mi + di, mj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= m or (ni == r-1 and nj == c-1): continue
            if not board[ni][nj]:  # 방문 안한 점
                board[ni][nj] = move_cnt + 1
                q.append((ni, nj, move_cnt + 1))

    print(res)

# 2번
if True:
    def backtrack(time, ci, cj):
        global ssum, min_res
        if time > t:
            return
        if ci == ei and cj == ej:
            ssum += 2  # 도착점 포함 안하기
            if min_res > ssum:
                min_res = ssum
            return

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            # 인덱스 밖, 건물, 출발점을 만나면 건너뛰기
            if ni < 0 or ni >= n or nj < 0 or nj >= n or not arr[ni][nj] or arr[ni][nj] == -1: continue
            ssum += arr[ni][nj]
            backtrack(time + 1, ni, nj)
            ssum -= arr[ni][nj]


    n, t = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    si, sj, ei, ej = 0, 0, 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == -1:
                si, sj = i, j
            elif arr[i][j] == -2:
                ei, ej = i, j

    min_res = int(1e9)
    ssum = 0
    backtrack(0, si, sj)

    if min_res == int(1e9):
        print(-1)
    else:
        print(min_res)

# 3번
if True:
    def get_result(arr):
        # 1. 한 나라의 승, 무, 패 합이 반드시 5 여야 함
        for i in range(6):
            nation = 0
            for j in range(3):
                nation += arr[i][j]
            if nation != 5: return 0
        # 2. 총 이긴 경기 수 = 총 진 경기 수
        whole = 0
        for k in range(6):
            whole += arr[k][0]
            whole -= arr[k][2]
        if whole: return 0
        # 3. 무승부는 대칭 관계여야 함
        draw = 0
        for z in range(6):
            if draw <= 0:
                draw += arr[z][1]
            else:
                draw -= arr[z][1]
        if draw: return 0

        # 1, 2, 3 모두 빠져나가면
        return 1


    infos = [[], [], [], []]
    for x in range(4):
        inp = list(map(int, input().split()))
        for y in range(0, 16, 3):
            infos[x].append(inp[y:y + 3])

    res_ls = []
    for info in infos:
        ans = get_result(info)
        res_ls.append(ans)

    print(' '.join(map(str, res_ls)))