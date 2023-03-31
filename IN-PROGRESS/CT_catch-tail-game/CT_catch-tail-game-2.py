import sys, math
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 머리, 꼬리, 나머지 팀원들의 방향 구하기
# 큐 써서 다시 짜기
def get_members_dir(team_no, i, j):
    head = []
    rest = []
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    order = 1  # 몇 번째 사람인지
    while q:
        ci, cj = q.popleft()
        # d = 0  # 의미 x 갱신되라고 써놓은 변수
        ai, aj, d = 0, 0, 0
        for d in range(4):
            ni, nj = ci + delta[d][0], cj + delta[d][1]
            if (0 <= ni < N and 0 <= nj < N) and not visited[ni][nj]:
                if arr[ni][nj][1] == 2:
                    ai, aj, d = ni, nj, (d + 2) % 4
                    break
                elif arr[ni][nj][1] == 3:
                    ai, aj, d = ni, nj, (d + 2) % 4
                    continue

        q.append((ai, aj))
        visited[ai][aj] = 1

        if arr[ci][cj][1] == 1:
            head = [(order, ci, cj, d)]
            arr[ci][cj] = [team_no, -1]
        elif arr[ci][cj][1] == 2:
            rest.append((order, ci, cj, d))
            arr[ci][cj] = [team_no, -order]
        elif arr[ci][cj][1] == 3:
            arr[ci][cj] = [team_no, -order]
            return head + rest + [(order, ci, cj, d)]
        order += 1


def all_move(idx, team):
    # 머리만 한 칸 이동하기
    hi, hj, hd = team[0][1:]
    ti, tj, td = team[-1][1:]
    nhi, nhj = hi + delta[hd][0], hj + delta[hd][1]
    while nhi < 0 or nhi >= N or nhj < 0 or nhj >= N or not arr[nhi][nhj][1] or (arr[nhi][nhj][1] < 0 and arr[hi][hj][1] > arr[nhi][nhj][1]):
        hd = (hd + 1) % 4
        nhi, nhj = hi + delta[hd][0], hj + delta[hd][1]
        # print('allmove')
    si, sj = nhi, nhj  # 머리 이동 완료
    team[0] = [idx, nhi, nhj, hd]
    arr[nhi][nhj] = [idx, -1]
    arr[hi][hj] = [0, 4]
    # arr[si][sj] = [0, 4]

    for pp in range(1, len(team)):
        pi, pj = team[pp][1:3]
        pd = (hd + 2) % 4  # 머리 뒷사람들 머리 따라 이동
        npi, npj = si + delta[pd][0], sj + delta[pd][1]
        while npi < 0 or npi >= N or npj < 0 or npj >= N or not arr[npi][npj][1] or (arr[npi][npj][1] < 0 and arr[pi][pj][1] < arr[npi][npj][1]):
            pd = (pd + 1) % 4
            npi, npj = si + delta[pd][0], sj + delta[pd][1]

        team[pp] = [idx, npi, npj, (pd+2) % 4]
        arr[npi][npj] = [idx, -(pp+1)]
        arr[pi][pj] = [0, 4]
        si, sj = npi, npj

    # 꼬리 부분 초기화
    arr[ti][tj] = [0, 4]
    # print(members_dir)
    # for a in arr:
    #     print(a)
    # print()


def ball_in(round_no, now_rc):
    global score

    if not round_no: round_no = 4
    if round_no > 2: now_rc = (N-1) - now_rc
    team_no = 0
    if round_no == 1:
        for j in range(N):
            if arr[now_rc][j][1] < 0:
                score += (abs(arr[now_rc][j][1])) ** 2
                team_no = arr[now_rc][j][0]
                break
    elif round_no == 2:
        for i in range(N-1, -1, -1):
            if arr[i][now_rc][1] < 0:
                score += (abs(arr[i][now_rc][1])) ** 2
                team_no = arr[i][now_rc][0]
                break
    elif round_no == 3:
        for j in range(N-1, -1, -1):
            if arr[now_rc][j][1] < 0:
                score += (abs(arr[now_rc][j][1])) ** 2
                team_no = arr[now_rc][j][0]
                break
    elif round_no == 4:
        for i in range(N):
            if arr[i][now_rc][1] < 0:
                score += (abs(arr[i][now_rc][1])) ** 2
                team_no = arr[i][now_rc][0]
                break
    print(score)
    change_dir(team_no)


def change_dir(team_no):
    # members_dir에서 바꾸기
    members_dir[team_no] = members_dir[team_no][::-1]
    for idx, member in enumerate(members_dir[team_no], start=1):
        mi, mj, md = member[1:]
        # print(member, d, (d+2) % 4)
        member[-1] = (md+2) % 4
        arr[mi][mj] = [team_no, -idx]


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상 순
N, M, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]
for nn in range(N):
    inp = list(map(int, input().split()))
    for nnn in range(N):
        arr[nn][nnn] = [0, inp[nnn]]  # 팀 번호, 이동선 or 멤버 번호


# 머리, 중간, 꼬리 팀원들의 위치와 방향 구하기
members_dir = [[] for _ in range(M+1)]
visited = [[0] * N for _ in range(N)]
mm = 1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j][1] == 1:  # 머리부터 시작
            members_dir[mm] = get_members_dir(mm, i, j)
            # for a in arr:
            #     print(a)
            # print()
            mm += 1

# 라운드 진행
score = 0
for round in range(1, K+1):
    for no in range(1, M+1):
        all_move(no, members_dir[no])
        for a in arr:
            print(a)
        print()

    r_no = math.ceil(round/N)
    mod_round = r_no % 4
    now_row = round - N*(r_no-1) - 1
    ball_in(mod_round, now_row)  # round = 0이면 4번임

    # for a in arr:
    #     print(a)
    # print()
print(score)