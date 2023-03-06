import sys
sys.stdin = open('input.txt')

from collections import deque

# 이렇게 따로 함수로 빼지말고 my_tomato 초반에 1 찾을 때 변수를 세워서 0을 세면 됨
# zerocnt = 0이면 익은 토마토가 없는 것
# def shu_bushu():
#     for i in range(N):
#         for j in range(M):
#             if box[i][j] == 0:  # 안 익은 게 하나라도 있으면 시작
#                 return True
#     return False


def my_tomato(box):
    level = 0
    while queue:
        si, sj, level = queue.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = si + di
            nj = sj + dj
            if (0 <= ni < N) and (0 <= nj < M):
                if not box[ni][nj]:  # 익지 않은 토마토만
                    box[ni][nj] = level + 1
                    queue.append((ni, nj, level+1))
    return level - 1

for _ in range(5):
    M, N = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(N)]

    res = 0  # 모두 다 익은 경우 출력하기 위함
    queue = deque()
    zero_cnt = 0

    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                queue.append((i, j, 1))
            elif not box[i][j]:
                zero_cnt += 1

    if zero_cnt:
        res = my_tomato(box)

    if res:
        for ii in range(N):
            for jj in range(M):
                if box[ii][jj] == 0:  # 안 익은 토마토가 있음
                    res = -1
                    break
    print(res)