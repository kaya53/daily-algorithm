import sys, math
from collections import deque

input = sys.stdin.readline
# sys.stdin = open('input.txt')

# 처음에 한번만 호출
# 이동선과 멤버 수를 찾는 함수
def bfs(si, sj):
    q = deque()
    q.append((arr[si][sj][1], si, sj))
    visited[si][sj] = 1
    line_tmp = [[1, si, sj]]
    m_cnt = 1
    while q:
        now_no, ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue

            if arr[ni][nj][1] == now_no or arr[ni][nj][1] == now_no + 1:
                if 1 < arr[ni][nj][1] <= 3:
                    m_cnt += 1
                    line_tmp.append([m_cnt, ni, nj])
                else:
                    line_tmp.append([-1, ni, nj])
                q.append((arr[ni][nj][1], ni, nj))
                visited[ni][nj] = 1
                break  # 하나 찾으면 끝내기; 선끼리 공백없이 붙어있는 경우는 조건에 따라 고려하지 않아도 됨

    return m_cnt, line_tmp


def move_team():
    for idx, ml in enumerate(move_line):
        ml.rotate(1)
        mem_cnt = members[idx]  # 각 팀의 멤버 수

        for nno in range(mem_cnt):
            ml[nno][0] = nno + 1
        try:
            ml[mem_cnt][0] = -1
        except: pass  # 이동선이 팀원으로 꽉 차있는 경우

        for no, ci, cj in ml:
            arr[ci][cj] = [idx, no]


def throw_ball(round_no, rc, direc):
    global score
    # print(round_no, row) # round_no == 0; 4n번째 라운드라는 의미
    if round_no % 2:  # 1, 3라운드 행은 가만히 있고 열이 움직임
        for j in direc:
            if arr[rc][j][1] > 0:  # 사람이 있음
                score += (arr[rc][j][1]) ** 2
                # print(arr[rc][j][1])
                change_dir(arr[rc][j][0])
                return  # 한 명만 맞추기
    else:  # 2, 4(0) 라운드; 열은 가만히 있고 행이 움직임
        for i in direc:
            if arr[i][rc][1] > 0:  # 사람이 있음
                score += (arr[i][rc][1]) ** 2
                change_dir(arr[i][rc][0])
                return  # 한 명만 맞추기


def change_dir(team_no):
    team_line = move_line[team_no]
    t_cnt = members[team_no]
    team_line.rotate(-t_cnt)
    team_line.reverse()
    for nno in range(t_cnt):
        team_line[nno][0] = nno + 1
    try:
        team_line[t_cnt][0] = -1
    except: pass  # 이동선이 팀원으로 꽉 차있는 경우

    # 변화 사항 격자에도 적용하기
    for no, ci, cj in team_line:
        arr[ci][cj] = [team_no, no]


N, M, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
for r in range(N):
    inp = list(map(int, input().split()))
    for c in range(N):
        arr[r][c] = [-1, inp[c]]

# 이동선 찾기
members = []
move_line = []
visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j][1] == 1 and not visited[i][j]:
            m_cnt, n_line = bfs(i, j)
            move_line.append(deque(n_line))
            members.append(m_cnt)


score = 0
for r_no in range(1, K+1):
    move_team()
    round_no = (math.ceil(r_no / N)) % 4
    row = ((r_no - 1) % N)
    if not round_no or round_no == 1:
        if not round_no: row = (N-1) - row
        throw_ball(round_no, row, range(N))
    elif round_no == 2 or round_no == 3:
        if round_no == 3: row = (N - 1) - row
        throw_ball(round_no, row, range(N-1, -1, -1))
print(score)
