import sys

sys.stdin = open('input.txt')


# 팰린드롬 판별 함수
def pelin(N):
    if len(N) == 1:
        return 'no'
    else:
        while len(N) > 1:
            if N[0] != N[-1]:
                return 'no'
            else:
                N = N[1:-1]
        return 'yes'
# if true: print yes, else: print no


while True:
    N = sys.stdin.readline().rstrip()
    if N == '0':
        break
    if N == N[::-1]:
        print('yes')
    else:
        print('no')
