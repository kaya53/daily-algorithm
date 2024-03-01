import sys

sys.stdin = open('input.txt')

from collections import deque


def solution(n, p1, p2, m, family):
    adj = [[] for _ in range(n+1)]
    for f1, f2 in family:
        adj[f1].append(f2)
        adj[f2].append(f1)
    # for a in adj:
      #  print(a)
    q = deque([(p1, 0)])  # 시작 사람 번호, 촌수
    visited = [0] * (n+1)
    visited[p1] = 1
    while q:
        ppl, cnt = q.popleft()
        # print(ppl, cnt)
        if ppl == p2: return cnt
        for nnext in adj[ppl]:
            # print(nnext)
            if visited[nnext]:
                continue
            q.append((nnext, cnt+1))
            visited[nnext] = 1
    return -1


N = int(input())
S, E = map(int, input().split())
M = int(input())
arr = [tuple(map(int, input().split())) for _ in range(M)]
print(solution(N, S, E, M, arr))