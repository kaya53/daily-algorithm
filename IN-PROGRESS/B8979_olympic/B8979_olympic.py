import sys

sys.stdin = open('input.txt')

# for _ in range(2):
N, K = map(int, input().split())
nations = [list(map(int, input().split())) for _ in range(N)]

sort_nations = sorted(nations, key=lambda x: (-x[1], -x[2], -x[3]))

score = 1
# print(sort_nations)
for i in range(N):
    # print(sort_nations[i][0], K)
    if sort_nations[i][0] == K: break
    if i and sort_nations[i-1][1:] != sort_nations[i][1:]:
        score += 1
    # print(i)
print(score)