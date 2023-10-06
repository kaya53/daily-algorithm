import sys

sys.stdin = open('input.txt')

def solution():
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    idx = n-1
    answer = 0
    while k:
        for i in range(idx, -1, -1):
            coin = coins[i]
            if k >= coin:
                cnt = k // coin
                k -= cnt*coin
                answer += cnt
                idx = i-1
                break
    return answer


# for _ in range(2):
print(solution())