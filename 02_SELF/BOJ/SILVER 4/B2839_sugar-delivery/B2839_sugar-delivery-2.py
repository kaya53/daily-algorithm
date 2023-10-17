import sys

sys.stdin = open('input.txt')


def solution(n):
    tot = 0
    while n > 0:
        if n % 5 == 0:
            tot += (n//5)
            return tot
        else:
            n -= 3
            tot += 1
        # print(tot, n)
    if n == 0: return tot
    return -1


# for _ in range(5):
print(solution(int(input())))