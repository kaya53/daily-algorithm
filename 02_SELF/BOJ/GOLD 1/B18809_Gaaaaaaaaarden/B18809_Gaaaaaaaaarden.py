# 230604 pypy 2992ms => 3시간 소요
# flower를 set으로 처리 => 3172ms
# flower를 int로 처리 => 2992ms(어쩌면 sys.stdin.readline 차이일수도)
# 유의할 점
# 1. 꽃이 된 곳에서는 더 이상 배양액이 퍼지지 않는다고 했음
# - 꽃이 되기 전에 이미 큐에 들어간 애들도 신경을 써줘야 한다!
# - 그래서 큐에서 popleft를 했을 때 이미 꽃이 된 애면 pass

import sys
# sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline


def comb_possible(idx, ci):
    if idx == T:
        # print(pos_choice)
        all_possible.append(list(pos_choice))
        return
    for ni in range(ci, lenP):
        pos_choice[idx] = possible[ni]
        comb_possible(idx+1, ni+1)
        pos_choice[idx] = ()


def comb_nutri(idx):
    if idx == T:
        # print(choice)
        for now_possible in all_possible:
            bfs(now_possible, choice)
        return

    for nnext in [3, 4]:
        if count[nnext] == 0: continue
        choice[idx] = nnext
        count[nnext] -= 1
        comb_nutri(idx+1)
        choice[idx] = 0
        count[nnext] += 1


def bfs(now_possible, nutri_choice):
    global max_flower

    flower = 0
    q = deque()
    # 시간, 초록 배양액, 빨강 배양액
    visited = [[[-1, 0, 0] for _ in range(M)] for _ in range(N)]
    for k in range(T):
        si, sj = now_possible[k]
        s_color = nutri_choice[k]
        # visited 해주기
        visited[si][sj][0] = 0
        visited[si][sj][s_color-2] = 1
        q.append((si, sj, s_color))

    time = 0
    while q:
        time += 1
        for _ in range(len(q)):
            ci, cj, now_color = q.popleft()
            # 꽃이 된 곳은 건너뛴다 => 이부분 때문에 몇몇 테케가 다르게 나왔었음
            if visited[ci][cj][1] and visited[ci][cj][2]: continue

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= M or not arr[ni][nj]: continue
                if -1 < visited[ni][nj][0] < time: continue

                if visited[ni][nj][0] == -1:  # 방문한 적 없음
                    visited[ni][nj][0] = time
                    visited[ni][nj][now_color-2] += 1
                    q.append((ni, nj, now_color))
                # 현재 타임에 방문했는데 나와 다른 색이 방문했었음
                elif visited[ni][nj][0] == time and (not visited[ni][nj][1] or not visited[ni][nj][2]):
                    visited[ni][nj][now_color-2] += 1
                    if visited[ni][nj][1] and visited[ni][nj][2]: flower += 1

    if max_flower < flower: max_flower = flower
    return


# for _ in range(10):
N, M, G, R = map(int, input().rstrip().split())
arr = [[] for _ in range(N)]
possible = []
for n in range(N):
    inp = list(map(int, input().rstrip().split()))
    arr[n] = inp
    for m in range(M):
        if inp[m] == 2: possible.append((n, m))

# nutri = ['G'] * G + ['R'] * R
T = G+R
count = {3: G, 4: R}
lenP = len(possible)

max_flower = -1

# 배양액 놓을 격자 고르기
pos_choice = [() for _ in range(T)]
all_possible = []
comb_possible(0, 0)
# print(all_possible)
# 선택된 격자에 어떤 배양액을 놓을 것인지
choice = [0] * T
comb_nutri(0)
print(max_flower)