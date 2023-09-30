# 소요시간 40분 => pypy 120ms
import sys

sys.stdin = open('input.txt')

delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def forward(r_no, cnt, robots, N, M, R):
    ci, cj, cd = robots[r_no]

    for _ in range(cnt):
        # print(ci, cj)
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            return f'Robot {r_no+1} crashes into the wall'
        check = check_crash(r_no, ni, nj, robots, R)
        if check: return f'Robot {r_no+1} crashes into robot {check+1}'

        ci, cj = ni, nj

    robots[r_no] = [ci, cj, cd]
    return True


def check_crash(me, ni, nj, robots, R):
    for you in range(R):
        if me == you: continue
        if (robots[you][0], robots[you][1]) == (ni, nj): return you
    return False


def rotate(r_no, order, cnt, robots):
    cd = robots[r_no][2]
    for _ in range(cnt):
        if order == 'L': cd = (cd+1) % 4
        elif order == 'R': cd = (cd-1) % 4
    robots[r_no][2] = cd
    return

def solution():
    M, N = map(int, input().split())
    R, O = map(int, input().split())  # 로봇 수, 명령 수
    robots = [input().split() for _ in range(R)]
    orders = [input().split() for _ in range(O)]

    for r in range(R):
        rj, ri, rd = robots[r]
        if rd == 'N': rd = 0
        elif rd == 'W': rd = 1
        elif rd == 'S': rd = 2
        else: rd = 3
        robots[r] = [N-int(ri), int(rj)-1, rd]
    # 시작
    for r_no, order, cnt in orders:
        r_no = int(r_no) - 1
        cnt = int(cnt)
        if order == 'F':
            res = forward(r_no, cnt, robots, N, M, R)
            if res is not True: return res
        else: rotate(r_no, order, cnt, robots)
    return 'OK'


print(solution())
