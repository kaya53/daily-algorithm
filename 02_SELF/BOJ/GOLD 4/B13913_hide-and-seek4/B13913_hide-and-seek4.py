# 230502 python 1804ms pypy 652ms

# 그리디적 사고
# => 발생할 수 있는 가장 최대인 100000 0을 넣어봤을 때 시간초과가 예상되었음

# 해결) 수빈이가 동생보다 앞에 있을 때는 -1씩 앞으로 가는 방법 밖에는 없다
# => 시간 초과가 나지 않기 위해서는 동생보다 앞에 있는 경우, 뒤에 있는 경우를 나눠야 한다

from collections import deque


def solve():
    q = deque()
    visited = [0] * 100001
    q.append((N, [N]))
    visited[N] = 1
    time = -1

    while q:
        time += 1
        for _ in range(len(q)):
            now, ls = q.popleft()
            if now == K:
                return time, ls

            for nnext in [2 * now, now - 1, now + 1]:
                if nnext < 0 or nnext > 100000 or visited[nnext]: continue
                q.append((nnext, ls + [nnext]))
                visited[nnext] = 1


N, K = map(int, input().split())
if N > K:
    print(N-K)
    print(*list(range(N, K-1, -1)))
else:
    res, ls = solve()
    print(res)
    print(*ls)
