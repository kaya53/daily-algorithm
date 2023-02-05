import sys

sys.stdin = open('input.txt')


# 재귀; 0120 통과 코드
def recur(k, n):
    if k == 0:  # 0층에서는 호수만큼 리턴
        return n
    if n == 1:  # 1호는 1
        return 1
    if k >= 1 and n > 1:  # 그 외는 재귀처리
        return recur(k - 1, n) + recur(k, n - 1)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    print(recur(k, n))


# 이전에 쓴 코드
# 호수만큼 1차원 배열을 만들고 층별로 배열 원소 바꾸기
t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n+1)]

    for x in range(k):
        for y in range(1, n):
            people[y] += people[y-1]
    print(people[-1])