# n의 크기가 큰 문제임 1<= n <= 100,000
import sys
import heapq


sys.stdin = open('input.txt')
input = sys.stdin.readline  # 아니 이거 쓰니까 python3 4036ms => 180ms됨 ...? 이렇게 차이가 난다고?
# for _ in range(2):
n = int(input())
hq = []
for _ in range(n):
    heapq.heappush(hq, int(input()))

res = 0
while len(hq) > 1:
    now1 = heapq.heappop(hq)
    now2 = heapq.heappop(hq)
    res += now1 + now2
    heapq.heappush(hq, now1+now2)
print(res)