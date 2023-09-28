import sys

sys.stdin = open('input.txt')


N = int(input())
num = [int(input()) for _ in range(N)]
d = [1] * (N)

print(num)
for i in range(N):
    for j in range(i):
        if num[j] < num[i]:
            print(num[i], num[j])
            d[i] = max(d[i], d[j]+1)
            print(d)
        # print()


