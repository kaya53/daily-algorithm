# 그리디
import sys

input = sys.stdin.readline

W, N = map(int, input().split()) # 무게, 금속 개수
stones = [tuple(map(int, input().split())) for _ in range(N)]
stones.sort(key=lambda x:x[1], reverse=True) # key에 x[0]까지 포함해서 틀렸음

tot = 0
for weight, price in stones:
  if W > weight:
    W -= weight
    tot += weight*price
  else:
    tot += W*price
    break

print(tot)