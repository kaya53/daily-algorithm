# 소요시간 20분 python 120ms
# 어떤 방까지 최소 얼마의 비용을 가지고 갈 수 있는 지
# => 비용: 흰 방으로 바꾸기
import sys

sys.stdin = open('input.txt')

from collections import deque


def solution(n, arr):
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[-1]*n for _ in range(n)]
    q = deque([(0,0,0)])
    visited[0][0] = 0

    while q:
        ci, cj, cnt = q.popleft()
        for di, dj in delta:
            ni, nj = ci+di, cj+dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n: continue
            if arr[ni][nj]:
                if visited[ni][nj] == -1 or visited[ni][nj] > cnt:
                    visited[ni][nj] = cnt
                    q.append((ni, nj, cnt))
            else:
                if visited[ni][nj] == -1 or visited[ni][nj] > cnt:
                    visited[ni][nj] = cnt+1
                    q.append((ni, nj, cnt+1))
    return visited[-1][-1]


N = int(input())
print(solution(N, [list(map(int, input())) for _ in range(N)]))