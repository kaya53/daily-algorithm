# 230531 python 168ms => 30분
import sys

sys.stdin = open('input.txt')


def comb(idx, ci):
    global min_cost
    if idx == num:
        pro, fat, glu, vit, price = 0, 0, 0, 0, 0
        for r in choice:
            pro += food[r][0]
            fat += food[r][1]
            glu += food[r][2]
            vit += food[r][3]
            price += food[r][4]

        if pro >= min_nutri[0] and fat >= min_nutri[1] and glu >= min_nutri[2]\
            and vit >= min_nutri[3] and min_cost >= price:
            min_cost = price
            cand.append((price, list(choice)))
        return

    for ni in range(ci, N+1):
        # now = food[ni]
        choice[idx] = ni
        comb(idx+1, ni+1)
        choice[idx] = 0


N = int(input())
min_nutri = list(map(int, input().split()))
food = [0] + [list(map(int, input().split())) for _ in range(N)]  # 단, 지, 탄, 비타민, 가격 순

min_cost = int(1e9)
cand = []
for num in range(1, N+1):
    choice = [0] * num
    comb(0, 1)

if cand:
    cand.sort()
    res = cand.pop(0)
    print(res[0])
    print(*res[1])
else:
    print(-1)
