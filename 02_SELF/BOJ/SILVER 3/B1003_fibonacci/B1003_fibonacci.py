# 소요시간 27분 pypy 148ms python 48ms
# dp, 메모이제이션 사용
# n-1, n-2번째까지 0, 1이 호출된 횟수를 더해서 n의 0, 1 호출 횟수를 구한다
# 그냥 피보나치로만 풀어도 되지만 시간 제한이 0.25초여서 메모이제이션이 필요하다고 판단
import sys

sys.stdin = open('input.txt')


def solution(num):
    global zero, one
    if num == 0:
        ls[0] = [1, 0]
        return [1, 0]
    elif num == 1:
        ls[1] = [0, 1]
        return [0, 1]
    if ls[num-2] == [0, 0]:
        ls[num-2] = solution(num-2)
    if ls[num-1] == [0, 0]:
        ls[num-1] = solution(num-1)
    ls[num] = [ls[num-2][0] + ls[num-1][0], ls[num-2][1] + ls[num-1][1]]
    return ls[num]


# for _ in range(2):
T = int(input())
for _ in range(T):
    n = int(input())
    ls = [[0, 0] for _ in range(n+1)]
    solution(n)
    print(*ls[-1])
