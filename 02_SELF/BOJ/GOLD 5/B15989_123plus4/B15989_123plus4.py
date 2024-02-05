# 소요시간 30분 python 804ms pypy 444ms
# n의 구성 중 1이 있는 것과 없는 것으로 크게 나눈다.
# - 1이 있는 것: 1과 다른 수로 구성
# - 1이 없는 것: 2, 3으로만 구성 => 222 33 모두 가능
# - i번째 = i-1번째 전체 합 + i-2번째에 1이 아닌 걸로만 구성된 것
    # - but 이렇게만 나누면 처음으로 33 같이 3으로만 구성된게 들어올 때 체킹이 안된다
    # - 그래서 i가 3의 배수일 때 +1을 또 해준다.
import sys

sys.stdin = open('input.txt')


def solution(n):
    memo = [[0, 0] for _ in range(n+1)]
    memo[1][0] = 1
    if n > 1: memo[2] = [1, 1]
    if n > 2: memo[3] = [2, 1]
    for i in range(4, n+1):
        # 1이 있는 부분은 그 전 요소의 합
        memo[i][0] = sum(memo[i-1])
        # 1이 없는 부분 => 2개 전 요소의 합
        memo[i][1] = memo[i-2][1]
        # 3의 배수 => += 1 해주기
        if i % 3 == 0: memo[i][1] += 1
    return sum(memo[n])


T = int(input())
for _ in range(T):
    print(solution(int(input())))