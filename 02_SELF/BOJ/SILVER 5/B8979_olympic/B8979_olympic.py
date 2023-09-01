# 소요시간 15분 96ms 
# 문제에서 나온 "내 등수는 나보다 더 잘한 나라 수 +1"라는 말만 잘 구현하면 됐음

import sys

sys.stdin = open('input.txt')

# for _ in range(2):
N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

target = []
for n in nations:
    if n[0] == K: target = n

better = same = 0
for nation in nations:
    if target == nation: continue

    if nation[1] > target[1]: better += 1
    elif nation[1] == target[1] and nation[2] > target[2]: better += 1
    elif nation[1] == target[1] and nation[2] == target[2] and\
        nation[3] > target[3]: better += 1
    elif nation[1] == target[1] and nation[2] == target[2] and nation[3] == target[3]: same += 1

print(better+1)