import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def binary_search(target):
    left = 0
    right = len(power_ls) - 1
    while left <= right:
        mid = (left + right) // 2
        if target <= power_ls[mid]: right = mid - 1
        else: left = mid + 1
    return name_ls[right+1]


N, M = map(int, input().split())
name_ls = []
power_ls = []
for _ in range(N):
    name, num = input().split()
    name_ls.append(name)
    power_ls.append(int(num))

for _ in range(M):
    print(binary_search(int(input())))



