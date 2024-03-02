import sys

sys.stdin = open('input.txt')


def solution(n, buildings):
    answer = 0
    stack = []
    for h in buildings:
        while stack and stack[-1] <= h:
            stack.pop()
        stack.append(h)
        print(stack)
        answer += len(stack) - 1  # 자기 자신 제외
    return answer


N = int(input())
arr = [int(input()) for _ in range(N)]
print(solution(N, arr))