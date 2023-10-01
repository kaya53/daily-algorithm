# 소요시간 1시간 pypy 132ms
# 틀린 이유: 디테일한 에러 처리에 애먹음
# 1. 감소하는 수는 0번부터 센다
# 2. 감소하는 수의 최대는 9876543210 즉, 1022번째 수이다
# 3. 오름차순으로 순서를 세야 하므로 백트래킹에서 숫자를 더해갈때는 
    # 가장 큰 자리수부터 더해나가고, 자리수를 뺴주면서 가야 한다
import sys

sys.stdin = open('input.txt')


def backtrack(digit, num, ci, x, n):
    global cnt, answer
    if answer >= 0: return

    if digit == 0:
        cnt += 1
        if cnt == n:
            answer = num
        return

    for ni in range(0, ci):
        num += ni*(10**(digit-1))
        backtrack(digit-1, num, ni, x, n)
        num -= ni * (10 ** (digit - 1))


def solution():
    n = int(input())
    for d in range(1, 11):
        backtrack(d, 0, 10, d, n) # digit, num, ci, x, cnt, n
        if cnt == n or cnt == 1022: break


cnt = -1
answer = -1
solution()
print(answer)
