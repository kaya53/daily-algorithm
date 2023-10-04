# 소요시간 30분 python 44ms
# 그리디
# - 매번 제일 저렴한 선택을 하면 됨
# => 브랜드 가격이 여러 개 나와 있어도 패키지로 제일 싼 곳, 낱개로 제일 싼 곳만 알면 됨

import sys

sys.stdin = open('input.txt')

def solution():
    n, m = map(int, input().split())

    price_pack = price_one = 1001
    for _ in range(m):
        p, o = map(int, input().split())
        if price_pack > p: price_pack = p
        if price_one > o: price_one = o
    # print(price_pack, price_one)

    cost = 0
    while n > 0:
        if n >= 6:
            if price_pack < 6*price_one:
                cost += price_pack
            else:
                cost += 6*price_one
            n -= 6
        else:
            if price_pack < n*price_one:
                cost += price_pack
            else:
                cost += n*price_one
            n = 0
    return cost


# for _ in range(6):
print(solution())

