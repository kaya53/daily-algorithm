import sys

sys.stdin = open('input.txt')

from collections import deque

### 방법 1: pypy로 하면 메모리 초과, python3로 하면 시간 초과 나옴
cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0: break

    rupee = [list(map(int, input().split())) for _ in range(n)]
    arr = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque([(0, 0)])
    arr[0][0] = rupee[0][0]

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue

            val = arr[ci][cj] + rupee[ni][nj]
            if not arr[ni][nj]:  # ni, nj칸으로 처음 온 경우
                arr[ni][nj] = val
                q.append((ni, nj))
            else:
                if arr[ni][nj] > val:
                    arr[ni][nj] = val
                    q.append((ni, nj))
        visited[ci][cj] = 1
    print(f'Problem {cnt}: {arr[-1][-1]}')

## 방법 2. 통과함
cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0: break

    rupee = [list(map(int, input().split())) for _ in range(n)]
    arr = [[float('inf')] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    q = deque([(0, 0, rupee[0][0])])
    arr[0][0] = rupee[0][0]

    while q:
        ci, cj, dist = q.popleft()
        if dist > arr[ci][cj]: continue

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            next_dist = dist + rupee[ni][nj]
            if arr[ni][nj] > next_dist:
                arr[ni][nj] = next_dist
                q.append((ni, nj, next_dist))

    print(f'Problem {cnt}: {arr[-1][-1]}')


## 최종 제출 코드
# 방법 1에서 불필요한 코드를 뺌 -> 근데 결국 2와 같아짐
# visited랑 arr[ni][nj]에 대한 if문 뺌
from collections import deque

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0: break

    rupee = [list(map(int, input().split())) for _ in range(n)]
    MAXI = 125**2*9
    arr = [[MAXI] * n for _ in range(n)]
    q = deque([(0, 0)])
    arr[0][0] = rupee[0][0]

    while q:
        ci, cj = q.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue

            val = arr[ci][cj] + rupee[ni][nj]
            if arr[ni][nj] > val:
                arr[ni][nj] = val
                q.append((ni, nj))
    print(f'Problem {cnt}: {arr[-1][-1]}')


## 최종 제출 코드 수정본
# deque를 heapq로 변경
# 성능상 오히려 안좋아짐 216ms -> 340ms

import heapq

cnt = 0
while True:
    cnt += 1
    n = int(input())
    if n == 0: break

    rupee = [list(map(int, input().split())) for _ in range(n)]
    MAXI = 125**2*9
    arr = [[MAXI] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0))
    arr[0][0] = rupee[0][0]

    while q:
        ci, cj = heapq.heappop(q)
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue

            val = arr[ci][cj] + rupee[ni][nj]
            if arr[ni][nj] > val:
                arr[ni][nj] = val
                heapq.heappush(q, (ni, nj))
                #q.append((ni, nj))
    print(f'Problem {cnt}: {arr[-1][-1]}')