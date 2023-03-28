import sys
# sys.stdin = open('input.txt')

input = sys.stdin.readline


def move_runner(si, sj, d):
    ni, nj = si + delta[d][0], sj + delta[d][1]
    if ni < 0 or ni >= n or nj < 0 or nj >= n:
        d = (d+2) % 4
        ni, nj = si + delta[d][0], sj + delta[d][1]
    # 움직이려는 칸에 술래가 있다면 움직이지는 않고 방향은 튼 상태로
    if [ni, nj] == [tagger[0], tagger[1]]: return [si, sj, d]  # 이 부분! 진짜 가지가지한다 지민아....
    return [ni, nj, d]


def runner_func():
    for idx, r in enumerate(runner):
        ri, rj, rd = r
        dist = abs(ri - tagger[0]) + abs(rj - tagger[1])
        if dist <= 3:
            runner[idx] = move_runner(ri, rj, rd)


def snail(corner, ci, cj, d, delta):
    global flag, before

    if not flag: corner = corner[::-1]
    ni, nj = ci + delta[d][0], cj + delta[d][1]
    if before < len(corner)-1 and (ni, nj) == corner[before+1]:
        if flag: d = (d+1)% 4
        else: d = (d-1) % 4
        before += 1
    elif (ni, nj) == (n//2, n//2):
        flag = True
        d = 0
        before = -1
    elif (ni, nj) == (0, 0):
        flag = False
        d = 2
        before = -1

    return [ni, nj, d]  # 술래의 다음 위치와 방향


def move_tagger():
    global tagger
    tagger = snail(corner, tagger[0], tagger[1], tagger[2], delta)
    ti, tj, td = tagger
    cnt = 0
    catch = runner
    for k in range(3):
        ni, nj = ti + delta[td][0]*k, tj + delta[td][1]*k
        # print(ni, nj)
        tmp = []
        for pp in catch:
            # for _ in range(len(catch)):
            pi, pj, d = pp
            if (pi, pj) == (ni, nj) and (pi, pj) not in tree:
                cnt += 1
            else: tmp.append([pi, pj, d])
        catch = tmp
    # print(catch, cnt)
    return catch, cnt


# 모서리 구하기
def get_corner():
    t = (n - 1) * 2
    ls = [0] * t
    u = 1
    for l in range(0, t - 1, 2):
        ls[l] = ls[l + 1] = u
        u += 1
    si, sj = tagger[:2]
    corner = []
    ci, cj = si, sj
    for x, s in enumerate(ls):
        d = x % 4
        ci, cj = ci + delta[d][0] * s, cj + delta[d][1] * s
        corner.append((ci, cj))
    return corner


delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 오른 아래 왼
# for _ in range(3):
n, m, h, k = map(int, input().split())
runner = [[] for _ in range(m)]
# runner = deque(runner)
for mm in range(m):
    i, j, d = map(int, input().split())
    if d == 1:  # 좌우 - 오른쪽 보고 시작
        runner[mm] = [i-1, j-1, 1]
    else:  # 상하 - 아래쪽 보고 시작
        runner[mm] = [i-1, j-1, 2]

tree = set()
for hh in range(h):
    y = tuple(map(lambda x: x-1, map(int, input().split())))
    tree.add(y)

tagger = [n//2, n//2, 0]  # 술래는 정중앙에서 시작
corner = get_corner()

score = 0
flag = True
before = -1
for time in range(1, k+1):  # k번 진행
    if not runner: break
    runner_func()
    runner, cnt = move_tagger()
    score += time*cnt
print(score)