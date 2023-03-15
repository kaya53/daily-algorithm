import sys

sys.stdin = open('input.txt')


# def subset(idx):
#     global mmin
#
#     if idx == n:
#         ssum = sum(choice)
#         if ssum >= b:
#             if mmin > ssum:
#                 mmin = ssum
#         return
#     choice[idx] = s[idx]  # 고르고
#     subset(idx + 1)  # 그 다음으로
#     choice[idx] = 0  # 안고르고
#     subset(idx + 1)  # 그 다음으로
def subset(idx, ssum):
    global mmin

    if idx == n:
        # ssum = sum(choice)
        if ssum >= b:
            if mmin > ssum:
                mmin = ssum
        return
    # choice[idx] = s[idx]  # 고르고
    subset(idx + 1, ssum+s[idx])  # 그 다음으로
    # choice[idx] = 0  # 안고르고
    subset(idx + 1, ssum)

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))

    mmin = int(1e9)
    choice = [0]*n
    subset(0, 0)  # ssum을 들고 다니는 방식으로 하니까 시간이 감소함
    print(f'#{tc} {mmin-b}')