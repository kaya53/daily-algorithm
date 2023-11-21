# sort를 쓰면 시간 초과가 난다
# heapq를 써야 시간 내에 들어옴
import sys, heapq

N = int(input())
classes = []
for _ in range(N):
  a, b = map(int, input().split())
  heapq.heappush(classes, (b, a))

now_e = 0
cnt = 0
while classes:
  e, s = heapq.heappop(classes)
  if s >= now_e:
    cnt += 1
    now_e = e
    # print(s,e)
print(cnt)