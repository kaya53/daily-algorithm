import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt')


def backtrack(idx, now):
    global mmax, mmin

    if idx == n-1:
        mmax = max(mmax, now)
        mmin = min(mmin, now)
        return

    for i in range(4):
        if not ops[i]: continue
        tmp = now
        ops[i] -= 1
        backtrack(idx+1, calc(i, now, nums[idx+1]))
        ops[i] += 1
        now = tmp


def calc(idx, now, nnext):
    if not idx:
        return now + nnext
    elif idx == 1:
        return now - nnext
    elif idx == 2:
        return now * nnext
    else:
        if now < 0:
            return (-now // nnext) * -1
        else:
            return now // nnext


# for _ in range(4):
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

mmax = -int(1e9)
mmin = int(1e9)
backtrack(0, nums[0])
print(mmax)
print(mmin)