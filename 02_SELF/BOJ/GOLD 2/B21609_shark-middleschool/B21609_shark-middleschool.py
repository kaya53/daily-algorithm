# 반시계 방향 90도 회전 하기
# for a in map(list, zip(*map(lambda x: x[::-1], arr))):
#     print(a)
import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(si, sj, clr, visited):  # 블록 그룹을 구함
    # global visited
    q = deque()
    q.append((si, sj))
    res = set()
    res.add((si, sj))
    zeros = []
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or visited[ni][nj]: continue
            if arr[ni][nj] < 0: continue  # 검정색 블록(-1), 빈칸(-2)
            if arr[ni][nj] > 0 and arr[ni][nj] != clr: continue # 다른 색인 경우
            q.append((ni, nj))
            res.add((ni, nj))
            visited[ni][nj] = 1
            if arr[ni][nj] == 0: zeros.append((ni, nj))
    for zi, zj in zeros:
        visited[zi][zj] = 0
    return len(zeros), len(res), res


def find_block(arr):
    global score  # 여기서 가장 큰 그룹을 찾으면 score 바로 갱신하기
    max_cnt = 1
    max_rainbow = 0
    max_blocks = []
    max_i, max_j = 0, 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                # visited[i][j] = 1
                rainbow, now_cnt, blocks = bfs(i, j, arr[i][j], visited)  # 블록 그룹 구하기
                if now_cnt < 2: continue
                if max_cnt < now_cnt:
                    max_cnt = now_cnt
                    max_rainbow = rainbow
                    max_blocks = blocks
                    max_i, max_j = i, j
                elif max_cnt == now_cnt:
                    if max_rainbow < rainbow:
                        max_rainbow = rainbow
                        max_blocks = blocks
                        max_i, max_j = i, j
                    elif max_rainbow == rainbow:
                        if max_i < i:
                            max_blocks = blocks
                            max_i, max_j = i, j
                        elif max_i == i and max_j < j:
                            max_blocks = blocks
                            max_i, max_j = i, j

    if max_cnt > 1:
        score += max_cnt**2
        # print('score', max_cnt, max_blocks)
        for bi, bj in max_blocks:
            arr[bi][bj] = -2
        return True # 블록 그룹까지 없앤 배열
    elif max_cnt == 1:  # 블록 그룹이 없는 경우
        return False


def gravity(arr):
    for j in range(n):  # 행 우선 순회; 열은 역순 순회
        for i in range(n-1, -1, -1):
            if arr[i][j] < 0: continue  # 검정 칸이나 빈 칸이면
            for k in range(i+1, n):  # 끝까지 내리기
                if arr[k][j] != -2: break  # 다음 칸이 빈 칸이 아니면
                arr[k-1][j], arr[k][j] = arr[k][j], arr[k-1][j]
    return arr

# for _ in range(3):
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

score = 0
while True:
    if not find_block(arr):  # 1, 2:
        print(score)
        break
    arr = gravity(arr)  # 3
    arr = gravity(list(map(list, zip(*map(lambda x: x[::-1], arr)))))