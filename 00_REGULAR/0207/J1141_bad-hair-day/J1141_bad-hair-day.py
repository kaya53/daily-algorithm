import sys

sys.stdin = open('input.txt')

N = int(input())
cows = [int(input()) for _ in range(N)]
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