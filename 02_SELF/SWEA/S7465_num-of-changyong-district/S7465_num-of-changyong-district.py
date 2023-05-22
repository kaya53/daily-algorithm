import sys

sys.stdin = open('s_input.txt')


def find(a):
    if a == parents[a]: return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_b == root_a: return False
    parents[root_b] = root_a
    return True


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    parents = list(range(N))
    for _ in range(M):
        s, e = map(lambda x: int(x)-1, input().split())
        union(s, e)
    res = 0
    for idx, p in enumerate(parents):
        if idx == p: res += 1
    print(f"#{tc} {res}")