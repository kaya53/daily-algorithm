# 230607 python 274ms => 2시간 30분 소요
# 포탄 공격하는 부분에서 이미 부서진 부분을 지나갈 수 없다는 것, 출발점은 공격 대상이 아니라는 것
# => 이 조건을 넣지 않아서 틀림..^^^^^^
# 이 문제에서는 격자 밖으로 나가면 반대편으로 오기 때문에 공격자를 만날 수도 있다
# => 그래서 ni, nj가 si, sj가 아닌 지를 체크해야 함
import sys
sys.stdin = open('input.txt')

from collections import deque


def choose_attack():
    cand = []
    min_power = 5001
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                if min_power > arr[i][j]: min_power = arr[i][j]

    for ii in range(N):
        for jj in range(M):
            if arr[ii][jj] == min_power:
                cand.append((min_power, attack_turn[ii][jj], ii+jj, jj))
    cand.sort(key=lambda x: [x[0], -x[1], -x[2], -x[3]])
    attacker = cand.pop(0)
    aj = attacker[3]
    ai = attacker[2] - aj
    return ai, aj


def choose_tower(ai, aj):
    cand = []
    max_power = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and (i, j) != (ai, aj):
                if max_power < arr[i][j]: max_power = arr[i][j]
    # print(max_power)
    for ii in range(N):
        for jj in range(M):
            if arr[ii][jj] == max_power and (ii, jj) != (ai, aj):
                cand.append((max_power, attack_turn[ii][jj], ii + jj, jj))

    cand.sort(key=lambda x: [-x[0], x[1], x[2], x[3]])
    receiver = cand.pop(0)
    rj = receiver[3]
    ri = receiver[2] - rj
    # print(ri, rj, receiver[0])
    return ri, rj


def attack(si, sj, ei, ej):
    attack_path = raser_bfs(si, sj, ei, ej)

    # 공격력 감소
    if attack_path:
        power = arr[si][sj]
        for ai, aj in attack_path:
            if (ai, aj) == (ei, ej): arr[ai][aj] -= power
            else: arr[ai][aj] -= power//2
        return attack_path
    
    # 레이저 공격이 안되서 포탄 공격함
    bomb = bomb_attack(si, sj, ei, ej)
    return bomb


def raser_bfs(si, sj, ei, ej):
    visited = [[0] * M for _ in range(N)]
    q = deque([(si, sj, [])])
    visited[si][sj] = 1
    while q:
        ci, cj, path_ls = q.popleft()
        if (ci, cj) == (ei, ej):  # 도착점 포함; 우선순위대로 bfs했으니까 도착하면 리턴하면 됨
            return path_ls

        for k in range(4):
            di, dj = delta[k]
            ni, nj = (ci + di) % N, (cj+dj) % M
            if visited[ni][nj] or arr[ni][nj] == 0 or (ni, nj) == (si, sj): continue
            q.append((ni, nj, path_ls+[(ni, nj)]))
            visited[ni][nj] = 1
    return False


def bomb_attack(si, sj, ei, ej):
    power = arr[si][sj]
    # print('power', power)
    arr[ei][ej] -= power
    attack_cand = []
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ni, nj = (ei + di) % N, (ej + dj) % M
        if arr[ni][nj] == 0 or (ni, nj) == (si, sj): continue  # 이거 넣으니까 답 나옴^^^^^
        attack_cand.append((ni, nj))
        arr[ni][nj] -= power//2
    return attack_cand


def check():
    cnt = 0  # 부서지지 않은 포탑 개수
    for i in range(N):
        for j in range(M):
            if arr[i][j] < 0:
                arr[i][j] = 0
            elif arr[i][j] > 0:
                cnt += 1
    return cnt


def repair_tower(ai, aj, ei, ej, attack_loc):
    # print(ei, ej)
    for i in range(N):
        for j in range(M):
            if (i, j) != (ai, aj) and (i, j) != (ei, ej) and arr[i][j] != 0 \
                    and (i, j) not in attack_loc:
                arr[i][j] += 1


delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우하좌상 순
# for _ in range(1):
# 행, 열, 턴 수
N, M, K = map(int, input().split())
# arr: 포탑 공격력
arr = [list(map(int, input().split())) for _ in range(N)]
attack_turn = [[0] * M for _ in range(N)]

for turn in range(1, K+1):
    ati, atj = choose_attack()
    attack_turn[ati][atj] = turn  # 공격턴 갱신
    arr[ati][atj] += N+M  # 공격자 공격력 증가
    eni, enj = choose_tower(ati, atj)

    attacked = attack(ati, atj, eni, enj)

    if check() <= 1: break  # 종료조건
    repair_tower(ati, atj, eni, enj, attacked)

res = 0
for ri in range(N):
    for rj in range(M):
        if res < arr[ri][rj]:
            res = arr[ri][rj]
print(res)