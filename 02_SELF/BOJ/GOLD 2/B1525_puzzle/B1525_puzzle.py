import sys
from collections import deque
# sys.stdin = open('input.txt')

input = sys.stdin.readline


def bfs(s_idx):
    q = deque()
    q.append((s_idx, puzzle, 0))
    while q:
        c_idx, now_pz, cnt = q.popleft()
        if now_pz == ['1', '2', '3', '4', '5', '6', '7', '8', '0']:
            return cnt
        for d in [-3, 3, -1, 1]:
            n_idx = c_idx + d
            if n_idx < 0 or n_idx > 8: continue
            if not c_idx % 3 and n_idx == c_idx - 1: continue
            if c_idx % 3 == 2 and n_idx == c_idx + 1: continue
            now_pz[c_idx], now_pz[n_idx] = now_pz[n_idx], now_pz[c_idx]

            if ''.join(now_pz) not in visited:
                q.append((n_idx, list(now_pz), cnt+1))
                visited.add(''.join(now_pz))
            # 퍼즐 바꿔 놨던거 취소
            now_pz[c_idx], now_pz[n_idx] = now_pz[n_idx], now_pz[c_idx]
    return -1


# input
puzzle = []
for _ in range(3): puzzle += input().split()

visited = set()
print(bfs(puzzle.index('0')))
