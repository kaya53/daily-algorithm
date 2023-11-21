# sort를 쓰면 시간 초과가 난다
# heapq를 써야 시간 내에 들어옴
import sys
input = sys.stdin.readline

N = int(input())
classes = [tuple(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x: [x[1], x[0]])
now_e = 0
cnt = 0
while classes:
  s, e = classes.pop(0)
  if s >= now_e:
    cnt += 1
    now_e = e
    # print(s,e)
print(cnt)


