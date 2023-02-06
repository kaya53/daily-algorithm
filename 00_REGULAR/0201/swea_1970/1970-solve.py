import sys

sys.stdin = open('input.txt')

T = int(input())  # 2
for tc in range(1, T+1):
    N = int(input())
    money_ls = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # res = [0] * 8

    for i in range(8):
        if N == 0: break  # 이 부분은 굳이 안넣어도 될 것 같다; N==0이면이 맞음
        money = money_ls[i]  # 여기를 빼고 for i in range(money_ls)로 바꿔도 될 거 같음
        if N // money:  # 어차피 몫이 없으면 0이 들어갈 테니까 이 if문도 없어도 될 것 같다
        # -> 그런데 이렇게 하면 연산을 덜 할 수 있다
            res[i] = N // money
            N %= money
    res = []
    for money in money_ls:
        res.append(N//money)  # 여기서 res에 쌓지 말고 바로 print를 해도 좋을 것 같다
        N %= money

    print(f'#{tc}')
    print(*res)