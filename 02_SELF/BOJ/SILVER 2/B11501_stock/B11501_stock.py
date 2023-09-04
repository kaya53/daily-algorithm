# 소요시간 1시간
# 저번에 풀었던 그리디 문제랑 똑같다고 보면 되는 데 왜 그걸 못 봤을까.... 하
# 지금보다 클 때 팔면 되니까 뒤에서 역순으로 보면 된다

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    prices = list(map(int, input().rstrip().split()))

    max_price = 0
    profit = 0
    for i in range(N-1, -1, -1):
        now = prices[i]
        if max_price < now:
            max_price = now
        elif max_price > now:
            profit += max_price - now
    print(profit)
    # print()