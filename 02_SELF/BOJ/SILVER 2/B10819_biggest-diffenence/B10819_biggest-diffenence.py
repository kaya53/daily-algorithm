import sys

sys.stdin = open('input.txt')

def calc(arr):
    res = 0
    for i in range(n-1):
        res += abs(arr[i] - arr[i+1])
    return res


def comb(idx):
    global mmax

    if idx == n:
        res = calc(choice)
        if mmax < res:
            mmax = res
        return
    for i in range(n):
        if not visited[i]:  # 같은 숫자가 여러번 나올 경우 안 걸러짐
            choice[idx] = nums[i]
            visited[i] = 1
            comb(idx+1)
            choice[idx] = 0
            visited[i] = 0


n = int(input())
nums = list(map(int, input().split()))
choice = [0] * n
visited = [0] * n
mmax = (2**31)*(-1)
comb(0)
print(mmax)