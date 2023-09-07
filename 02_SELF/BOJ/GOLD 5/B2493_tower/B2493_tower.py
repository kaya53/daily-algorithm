# 소요시간 20분 pypy 344ms
# - 스택을 이용하는 것만 파악하면 쉽게 풀리는 문제
# - 스택을 써야 하는 걸 어떻게 알 수 있을까?
# 1. 비교의 진행 방향이 한 방향이다
# - 레이저가 왼쪽으로만 나아감
# - 탑이 왼쪽에서 오른쪽으로 배열되어 있음
# => 나보다 왼쪽에 큰 것 하나만 찾으면 됨
# 2. 비교해야 할 탑의 개수(N)이 매우 크다
# - N이 50만까지이므로 바로 생각나는 for문으로 해결하면 O(N*N)이 나와서 백퍼 터진다
# - O(N)으로 할 수 있는 방법을 생각해야 함
# => 현재 볼 탑보다 작은 탑들을 보관해 놓을 자료 구조가 필요하다는 것을 생각할 수 있음

import sys

sys.stdin = open('input.txt')

N = int(input())
towers = list(map(int, input().split()))
stack = []
res = [0] * N
for i in range(N-1, -1, -1):
    now_tower = towers[i]
    if not stack or (stack and stack[-1][0] > now_tower):
        stack.append((towers[i], i))
    else:
        while stack and stack[-1][0] < now_tower:
            top_tower, top_idx = stack.pop()
            res[top_idx] = i+1
        stack.append((now_tower, i))
print(*res)
