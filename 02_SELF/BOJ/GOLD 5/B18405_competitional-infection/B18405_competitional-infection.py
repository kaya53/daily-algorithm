import sys
from collections import deque

# sys.stdin = open('input.txt')
input = sys.stdin.readline


# for _ in range(2):
n, k = map(int, input().rstrip().split())
arr = [[] for _ in range(n)]
# virus_dict = {}
q = []
init = 0
for nn in range(n):
    inp = list(map(int, input().rstrip().split()))
    arr[nn] = inp
    for mm in range(n):
        if inp[mm]:
            q.append((inp[mm], nn, mm))
            init += 1
q.sort(key=lambda x: x[0])
q = deque(q)
s, ei, ej = map(int, input().rstrip().split())
ei -= 1
ej -= 1

time = 0
cnt = init

while q:
    time += 1
    if time > s:
        print(arr[ei][ej])
        break
    if cnt == n*n:
        print(arr[ei][ej])
        break
    for _ in range(len(q)):
        virus_no, vi, vj = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = vi + di, vj + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n or arr[ni][nj]: continue
            arr[ni][nj] = virus_no
            q.append((virus_no, ni, nj))
            cnt += 1
