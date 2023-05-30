# 230520 python 84ms => 1시간 소요
# 틀린 이유
# 1. value error : sys.stdin.readline을 쓰면 개행문자까지 다 받아와서 이 에러가 생길 수 있다.
# 2. 회전시킬 때 처음엔 수직 수평 모두 left를 (+1, +1), right를 (-1, -1)로 옮겼다.
# - 이걸 수직일 때 left(1, -1), right(-1, 1), 수평일 때 left(-1, 1), right(1, -1)로 바꿔주니까 통과함
# - 근데 솔직히 왜 맞고 왜 틀린 지 모르겠음
import sys

# sys.stdin = open('input.txt')

from collections import deque


def can_rotate(now_wood, delta):
    for di, dj in delta:
        for ci, cj in now_wood:
            ni, nj = ci + di, cj + dj
            if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 1: return False
    return True


def bfs(start):
    q = deque([(start, 0)])
    visited.add(start)
    while q:
        now_wood, cnt = q.popleft()
        left, mid, right = now_wood

        if now_wood == end or now_wood[::-1] == end:
            return cnt
        # 이동
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
            for ci, cj in now_wood:
                ni, nj = ci + di, cj + dj
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == 1: break
            else:
                nnext = ((left[0]+di, left[1]+dj), (mid[0]+di, mid[1]+dj), (right[0]+di, right[1]+dj))
                if nnext in visited: continue
                q.append((nnext, cnt+1))
                visited.add(nnext)

        # 회전
        if (left[0] == mid[0] == right[0]) and (left[1] + 2 == mid[1] + 1 == right[1]):  # 수평
            if can_rotate(now_wood, [(-1, 0), (1, 0)]):
                nnext = ((left[0]-1, left[1]+1), mid, (right[0]+1, right[1]-1))
                if nnext in visited: continue
                q.append((nnext, cnt+1))
                visited.add(nnext)
        else:  # 수직
            if can_rotate(now_wood, [(0, -1), (0, 1)]):
                nnext = ((left[0] + 1, left[1] - 1), mid, (right[0] - 1, right[1] + 1))
                if nnext in visited: continue
                q.append((nnext, cnt+1))
                visited.add(nnext)
    return 0


# for _ in range(3):
N = int(input())
arr = [[] for _ in range(N)]

wood = []
end = []
for n in range(N):
    inp = list(map(str, input()))
    for m in range(N):
        if inp[m] == 'B':
            inp[m] = '0'  # 통나무
            wood.append((n, m))
        elif inp[m] == 'E':
            inp[m] = '0'  # 종착점
            end.append((n, m))
    arr[n] = list(map(int, inp))

end = tuple(end)
visited = set()
print(bfs(tuple(wood)))