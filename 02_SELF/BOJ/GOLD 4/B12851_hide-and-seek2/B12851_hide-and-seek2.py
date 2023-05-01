
from collections import deque


def bfs():
    q = deque()
    visited = [-1] * 100001
    visited[N] = 0
    q.append(N)
    min_time = time = -1
    cnt = 0

    while q:
        time += 1
        for _ in range(len(q)):
            now = q.popleft()
            if now == K:
                min_time = time
                cnt += 1
            for nnext in [now - 1, now + 1, now * 2]:
                if nnext < 0 or nnext > 100000: continue
                # if now == K or visited[nnext] == time+1:  # 조건을 이렇게 적었을 때는 답이 제대로 안나왔음

                # 같은 최단 시간으로 방문한 경우만 다음 큐에 넣어준다
                # 더 긴 시간으로 nnext 지점까지 왔다면 동생한테까지 갈 수 있다 쳐도 최단 시간을 보장하지 않으므로 볼 필요가 없다.
                # 방문 표시가 되지 않은 곳에 처음으로 왔다면 bfs이기 때문에 무조건 최단을 보장한다.
                if visited[nnext] == time+1:
                    q.append(nnext)
                elif visited[nnext] == -1:  # 방문하지 않은 경우
                    visited[nnext] = time + 1
                    q.append(nnext)

        if min_time > -1:
            return min_time, cnt


N, K = map(int, input().split())
print(*bfs(), sep='\n')
