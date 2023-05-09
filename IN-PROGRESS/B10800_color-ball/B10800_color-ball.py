import sys

sys.stdin = open('input.txt')

# for _ in range(2):
N = int(input())
balls = [() for _ in range(N)]
color_sum = [0] * 200001
size_ls = [0] * 2001
max_color = 0
for n in range(N):
    clr, s = map(int, input().split())
    balls[n] = (n, clr, s)
    # color_sum[clr] += s
    # if max_color < clr: max_color = clr
print(balls)
balls.sort(key=lambda x: x[2])  # 큰 공 제외하려고
total = 0
for idx, cs in enumerate(balls):
    no, color, size = cs
    total += size
    color_sum[color] += size
    print(no, total, color_sum[:16])



