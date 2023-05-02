from collections import deque


def solve():
    q = deque()
    visited = [0] * 100001
    q.append(N)
    visited[N] = 1
    time = -1

    while q:
        time += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == K: return time

            for nnext in [now-1, now+1]:
                if nnext < 0 or nnext > 100000 or visited[nnext]: continue
                q.append(nnext)
                visited[nnext] = 1
            
            # 순간 이동
            tmp = now
            while 0 < tmp < K:
                tmp *= 2
                if tmp == K: return time
                for tnext in [tmp-1, tmp+1]:
                    if tnext < 0 or tnext > 100000 or visited[tnext]: continue
                    q.append(tnext)
                    visited[tnext] = 1


N, K = map(int, input().split())
res = solve()
print(res)
