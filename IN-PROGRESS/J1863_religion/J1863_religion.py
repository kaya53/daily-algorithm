import sys

sys.stdin = open('input.txt')


def find(a):
    if parents[a] < 0: return a
    parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_b == root_a: return False
    parents[root_a] += parents[root_b]
    parents[root_b] = root_a
    return True


N, M = map(int, input().split())
parents = [-1] * N

for _ in range(M):
    s, e = map(lambda x: int(x)-1, input().split())
    union(s, e)
res = 0
for p in parents:
    if p < 0: res += 1
print(res)
