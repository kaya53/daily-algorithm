# 230607 python 132ms => 2시간 ~ 2시간 30분 소요
# 설계 꼼꼼히 하고 문제 풀자!!
# 틀린 이유
# 1. 설계 꼼꼼히 안 함
# 2. 라운드 계산 틀림

import sys
from collections import deque

# input = sys.stdin.readline
sys.stdin = open('input.txt')


# 여기서 선을 그룹 번호로 바뀌면 제대로 구해지지 않음
def get_team(si, sj):
    q = deque([(si, sj, 1)])
    visited[si][sj] = 1
    # arr[si][sj] = team_no
    cnt = 1
    team = deque([(si, sj)])
    while q:
        ci, cj, now = q.popleft()

        for di, dj in delta:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or visited[ni][nj]: continue
            if arr[ni][nj] == now or arr[ni][nj] == now+1:
                q.append((ni, nj, arr[ni][nj]))
                team.append((ni, nj))
                visited[ni][nj] = 1
                if 1 <= arr[ni][nj] <= 3: cnt += 1
    return team, cnt


def move():
    for idx in range(1, M+1):
        q = team_q[idx]
        q.rotate()
        k = 1
        # 움직인 후 이동선의 팀원들 마킹
        for ci, cj in q:
            if k <= team_cnt[idx]:
                arr[ci][cj] = (idx, k)
                k += 1
            else:  # 이동선
                arr[ci][cj] = 4


def get_round_no(round_no):
    k, v = divmod(round_no, N)
    if not k % 4:  # 1 - n
        return throw_and_score('r', v, range(N))
    elif k % 4 == 1:  # n+1 ~ 2n
        return throw_and_score('c', v, range(N-1, -1, -1))
    elif k % 4 == 2:  # 2n+1 ~ 3n
        return throw_and_score('r', N-v-1, range(N-1, -1, -1))
    else:  # 3n+1 ~ 4n
        return throw_and_score('c', N-v-1, range(N))


def throw_and_score(flag, rc, throw_range):
    if flag == 'r':
        for jj in throw_range:
            if arr[rc][jj] != 0 and arr[rc][jj] != 4: return arr[rc][jj]
    else:
        for ii in throw_range:
            if arr[ii][rc] != 0 and arr[ii][rc] != 4: return arr[ii][rc]


def change_dir(grp_no):
    q = team_q[grp_no]
    tmp = []
    idx = 0
    while idx < team_cnt[grp_no]:
        tmp.append((q.popleft()))
        idx += 1
    tmp = tmp[::-1]  # 팀원끼리 뒤집기
    q.reverse()  # 나머지 이동선 뒤집기
    tmp += q  # 뒤집은 것끼리 합치기
    return deque(tmp)


delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 팀 별 이동선, 팀 별 멤버 수 알아오기
team_q = [deque() for _ in range(M+1)]
team_cnt = [0] * (M+1)
visited = [[0] * N for _ in range(N)]

tk = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            t, c = get_team(i, j)
            team_q[tk] = t
            team_cnt[tk] = c
            tk += 1

score = 0
for r_no in range(K):
    # 한 칸씩 이동
    move()
    res = get_round_no(r_no)
    if res:
        grp, sc = res
        score += sc**2
        # 점수를 얻은 팀만 방향 바꾸기
        team_q[grp] = change_dir(grp)

print(score)
