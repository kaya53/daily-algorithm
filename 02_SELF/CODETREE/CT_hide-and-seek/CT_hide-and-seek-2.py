# 230605 python 154ms => 1시간 ~ 1시간 30분 소요
# 유의할 점
# 1. 달팽이 돌릴 때 역방향, 정방향 돌릴 때 방향 전환 처리!
# - 처음에 tag_flag를 제대로 전환해주지 않음
# - corner set에 (N//2, N//2)가 들어가 있지 않아서 제대로 방향이 안바뀌었음
import sys

sys.stdin = open('input.txt')


def move_runner():
    # print(runner)
    for no in range(M):
        if not runner[no]: continue  # 잡힌 도망자
        ci, cj, cd = runner[no]
        # 거리가 3 초과면 이동 안함
        if abs(seek_i-ci) + abs(seek_j-cj) > 3: continue
        ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            cd ^= 1  # 방향 전환
            ni, nj = ci + delta[cd][0], cj + delta[cd][1]
        # 움직이려는 자리가 술래 자리면 움직이지 않음
        if (ni, nj) == (seek_i, seek_j): continue
        runner[no] = [ni, nj, cd]  # 이동 완료
    # print(runner)


def move_tagger():
    global seek_i, seek_j, seek_d, tag_flag
    # tag_flag = True: 달팽이 정방향, False: 달팽이 역방향
    ci, cj, cd = seek_i, seek_j, seek_d
    ni, nj = ci + c_delta[cd][0], cj + c_delta[cd][1]
    if (ni, nj) in corner:
        if (ni, nj) == (0, 0):
            cd = 2
            tag_flag = False
        elif (ni, nj) == (N//2, N//2):
            cd = 0
            tag_flag = True
        else:
            if tag_flag: cd = (cd+1) % 4
            else: cd = (cd-1) % 4
    # 술래 이동 완료
    seek_i, seek_j, seek_d = ni, nj, cd


def get_corner():
    cor = set()
    ci, cj = N//2, N//2
    cor.add((ci, cj))
    cd = 0
    for k in range(1, N+1):
        for _ in range(2):
            ni, nj = max(0, ci + c_delta[cd][0]*k), max(0, cj + c_delta[cd][1]*k)
            cd = (cd + 1) % 4
            cor.add((ni, nj))
            if (ni, nj) == (0, 0): return cor
            ci, cj = ni, nj


def get_score():
    cnt = 0
    for k in range(3):
        ni, nj = seek_i + c_delta[seek_d][0]*k, seek_j + c_delta[seek_d][1]*k
        if (ni, nj) in tree: continue  # 나무가 있는 칸은 패스
        for r_no in range(M):
            if not runner[r_no]: continue
            ri, rj = runner[r_no][:2]
            if (ni, nj) == (ri, rj): # 잡힘
                cnt += 1
                runner[r_no] = None
    return cnt


c_delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌 // 하우상좌
delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]  # 좌우하상
# for _ in range(3):
N, M, H, K = map(int, input().split())
runner = [[0, 0, 0] for _ in range(M)]
for m in range(M):
    i, j, d = map(int, input().split())
    runner[m] = [i-1, j-1, d]

tree = set()
for t in range(H):
    tree.add(tuple(map(lambda x: int(x)-1, input().split())))

# 달팽이 돌 코너 찾기
corner = get_corner()
# print(corner)

seek_i, seek_j, seek_d = N//2, N//2, 0
tag_flag = True
score = 0
for turn in range(1, K+1):
    move_runner()
    move_tagger()
    score += turn * get_score()
    # print(score)
print(score)