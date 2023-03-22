import sys
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline
# for _ in range(4):
A, B, end_a, end_b = map(int, input().split())

q = deque()
q.append((0, 0, 0))
res = 0
visited = {}
visited[(0, 0)] = 1

while q:
    # print(q)
    now_a, now_b, cnt = q.popleft()
    if now_a == end_a and now_b == end_b:
        print(cnt)
        break

    for i in range(6):
        next_a, next_b = now_a, now_b
        if i == 0:
            next_a = A
        elif i == 1:
            next_b = B
        elif i == 2:
            next_a = 0
        elif i == 3:
            next_b = 0
        elif i == 4:  # a, b 순
            if now_a <= B-now_b:
                next_b = now_b + now_a
                next_a = 0
            else:
                next_b = B
                next_a = now_a - (B-now_b)
        elif i == 5:  # b, a 순
            if now_b <= A-now_a:
                next_a = now_b + now_a
                next_b = 0
            else:
                next_a = A
                next_b = now_b - (A-now_a)
        tp = (next_a, next_b)
        if visited.get(tp): continue # 이미 고른 적 있는 조합
        q.append((next_a, next_b, cnt+1))
        visited[tp] = 1

else:
    print(-1)
