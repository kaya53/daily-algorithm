from collections import deque

def bfs():
    q = deque()
    visited = [-1] * 100000
    visited[N] = 0
    q.append(N)
    cnt = min_time = 0
    time = -1
    while q:
        time += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == K:  # 여기서 같은 걸 찾는 과정에서 시간이 오래걸리는 것 같음
                min_time = time
                cnt += 1
            for nnext in [now - 1, now + 1, now * 2]:
                if nnext < 0 or nnext > 100000: continue
                if visited[nnext] < time: visited[nnext] = time
                q.append(nnext)
        if min_time:
            return min_time, cnt


N, K = map(int, input().split())
print(bfs())
