import sys

sys.stdin = open('input.txt')

def solution():
    n = int(input())

    answer = 0

    if not n % 5:
        return n // 5
    else:
        while n:
            # print(n)
            n -= 3
            answer += 1
            if not n % 5:
                return answer + n // 5
            elif n == 1 or n == 2:
                return -1
            elif n == 0:
                return answer


# for _ in range(5):
print(solution())
