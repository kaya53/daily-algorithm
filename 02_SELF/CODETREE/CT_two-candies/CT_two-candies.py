# 230605 python 115ms => 2시간 ~ 2시간 30분 소요
# 유의할 점
# 1. 두 개의 구슬을 기울이는 코드!
# - 일단 각각 기울인 다음에 두 구슬이 같은 위치에 있으면 두 구슬이 같은 행/열에 있었다는 의미이므로
# - 더 많이 움직인 구슬에 더해준 di, dj만큼 한 번 빼준다

import sys

sys.stdin = open('input.txt')

from collections import deque


def slide(k, ci, cj):
    di, dj = delta[k]
    cnt = 0  # 움직인 횟수
    while arr[ci+di][cj+dj] != '#' and arr[ci][cj] != 'O':
        ci += di
        cj += dj
        cnt += 1
    return (ci, cj), cnt, arr[ci][cj] == 'O'


def bfs():
    q = deque([(red, blue)])
    visited.add((red, blue))
    cnt = 0
    while q:
        cnt += 1
        if cnt > 10: return -1  # 10번 이내로 안되면 -1 출력
        for _ in range(len(q)):
            now_red, now_blue = q.popleft()

            for k in range(4):
                next_red, r_cnt, is_exit_red = slide(k, *now_red)
                next_blue, b_cnt, is_exit_blue = slide(k, *now_blue)

                # 같은 방향으로 기울어졌을 경우
                if next_red == next_blue:
                    if r_cnt > b_cnt:  # BR의 형태
                        next_red = next_red[0] - delta[k][0], next_red[1] - delta[k][1]
                    else:  # RB의 형태
                        next_blue = next_blue[0] - delta[k][0], next_blue[1] - delta[k][1]

                if is_exit_blue: continue  # 어떤 경우던 파란 공이 빠지면 안됨
                if is_exit_red and not is_exit_blue: return cnt  # 빨간 공만 빠졌으면 성공

                if (next_red, next_blue) in visited: continue
                q.append((next_red, next_blue))
                visited.add((next_red, next_blue))
    # 10번 이하로 기울였지만 안되서 빠져나온 경우
    return -1


delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# for _ in range(2):
N, M = map(int, input().split())
arr = [[] for _ in range(N)]
red = -1, -1
blue = -1, -1
end = -1, -1
for n in range(N):
    inp = list(map(str, input()))
    arr[n] = inp
    for m in range(M):
        if inp[m] == 'R': red = n, m
        elif inp[m] == 'B': blue = n, m
        elif inp[m] == 'O': end = n, m

visited = set()
print(bfs())
