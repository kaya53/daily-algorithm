from collections import deque

R, C, K = map(int, input().split())
board = [[0] * C for _ in range(R)]
check = []
heater = []
for i in range(R):
    tmp = list(map(int, input().split()))
    for j in range(C):
        if tmp[j] == 5:
            check.append((i, j))
        elif tmp[j] > 0:
            heater.append((i, j, tmp[j]))
W = int(input())
wall = []
for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        wall.append((x - 1, y - 1, x - 2, y - 1))
        wall.append((x - 2, y - 1, x - 1, y - 1))
    else:
        wall.append((x - 1, y - 1, x - 1, y))
        wall.append((x - 1, y, x - 1, y - 1))
choco = 0
direction = ((), ((0, 1), (1, 1), (-1, 1)), ((0, -1), (1, -1), (-1, -1)),
             ((-1, 0), (-1, 1), (-1, -1)), ((1, 0), (1, 1), (1, -1)))
wall_check = [[], [[[0, 0, 0, 1]], [[0, 0, 1, 0], [1, 0, 1, 1]], [[0, 0, -1, 0], [-1, 0, -1, 1]]],
              [[[0, 0, 0, -1]], [[0, 0, 1, 0], [1, 0, 1, -1]], [[0, 0, -1, 0], [-1, 0, -1, -1]]],
              [[[0, 0, -1, 0]], [[0, 0, 0, 1], [0, 1, -1, 1]], [[0, 0, 0, -1], [0, -1, -1, -1]]],
              [[[0, 0, 1, 0]], [[0, 0, 0, 1], [0, 1, 1, 1]], [[0, 0, 0, -1], [0, -1, 1, -1]]]]

def wall_ok(tx, ty, dd, ddir):
    for walls in wall_check[dd][ddir]:
        ntx = tx + walls[0]
        nty = ty + walls[1]
        ntx2 = tx + walls[2]
        nty2 = ty + walls[3]
        if (ntx, nty, ntx2, nty2) in wall:
            return False
    return True


def heater_wind(x, y, d):
    visited = [[False] * C for _ in range(R)]
    q = deque()
    sx, sy = x + direction[d][0][0], y + direction[d][0][1]
    if sx < 0 or sx >= R or sy < 0 or sy >= C:
        return
    q.append([sx, sy, 4])
    visited[sx][sy] = True
    board[sx][sy] += 5
    while q:
        x, y, temp = q.popleft()
        for dir in range(3):
            nx = x + direction[d][dir][0]
            ny = y + direction[d][dir][1]
            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and temp > 0:
                    if wall_ok(x, y, d, dir):
                        visited[nx][ny] = True
                        board[nx][ny] += temp
                        q.append([nx, ny, temp - 1])


dx,dy = (0,0,0,-1,1),(0,1,-1,0,0)

def temperature():
    graph = [[0] * C for _ in range(R)]
    visited = [[False] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:

                for mov in range(1, 5):
                    nx = i + dx[mov]
                    ny = j + dy[mov]

                    if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                        if wall_ok(i, j, mov, 0):
                            temp = abs(board[i][j] - board[nx][ny]) // 4
                            if board[i][j] > board[nx][ny]:
                                graph[i][j] -= temp
                                graph[nx][ny] += temp
                            elif board[i][j] < board[nx][ny]:
                                graph[i][j] += temp
                                graph[nx][ny] -= temp
                visited[i][j] = True
    for i in range(R):
        for j in range(C):
            board[i][j] += graph[i][j]
    return board


edge = (((0, 1), (0, C)), ((1, R-1), (0, 1)), ((1, R-1), (C - 1, C)), ((R - 1, R), (0, C)))
while True:
    # 1. 온풍기 바람
    for h in range(len(heater)):
        hx, hy, hd = heater[h]
        heater_wind(hx, hy, hd)

    # 2. 온도 조절
    board = temperature()

    # 3. 온도 1이상인 가장 바깥쪽 칸의 온도 1씩 감소
    for e in edge:
        xs, xe = e[0]
        ys, ye = e[1]
        for i in range(xs, xe):
            for j in range(ys, ye):
                if board[i][j] > 0:
                    board[i][j] -= 1

    # 4. 초콜릿 하나 먹는다.
    choco += 1
    if choco > 100:
        print(101)
        break
    # 5. 조사하는 모든 칸 온도 K이상인지 검사 하고 맞으면 중단 아니면 다시 시작
    flag = 1
    for x, y in check:
        if board[x][y] < K:
            flag = 0
            break
    if flag:
        print(choco)
        break
for b in board:
    print(b)