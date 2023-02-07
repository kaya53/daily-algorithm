import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
cows = deque(int(input()) for _ in range(N))
# print(cows)

# 시간 초과
# res = 0
# for i in range(N-1):
#     cnt = 0
#     for j in range(i+1, N):
#         if cows[j] < cows[i]:
#             cnt += 1
#         else: break
#     res += cnt
# print(res)


## 스택으로 풀기
stack = deque()
cnt = 0
while cows:
    now_cow = cows.popleft()
    while stack and stack[-1] <= now_cow:  # 다음에 들어올 소가 스택에 있는 마지막 소보다 작거나 같으면
        stack.pop()
    stack.append(now_cow)  # 다 빼고 넣건, 바로 넣건 어느 경우든 들어가긴 한다
    cnt += len(stack) - 1  # 들어갔으면 cnt를 갱신해준다
print(cnt)
