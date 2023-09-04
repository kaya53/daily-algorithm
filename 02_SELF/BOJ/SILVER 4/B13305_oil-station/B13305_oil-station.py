# 소요시간 15분 120ms ; 구글 참고함
# 매 도시를 지날 때마다,
# 현재 도시의 기름 가격과 여태까지 가장 저렴한 기름 가격을 비교해서
# 다음 도시만 넘어가면 됨

import sys

sys.stdin = open('input.txt')

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_oil = 1000000000
res = 0
for i in range(N-1):
    now_oil = prices[i]
    if min_oil > now_oil: min_oil = now_oil
    res += (roads[i]*min_oil)
print(res)

