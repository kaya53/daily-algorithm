import sys

sys.stdin = open('input.txt')

def solution():
    n = int(input())
    times = list(map(int, input().split()))
    times.sort()

    answer = 0
    now = 0
    for time in times:
        now += time
        answer += now
    return answer

print(solution())