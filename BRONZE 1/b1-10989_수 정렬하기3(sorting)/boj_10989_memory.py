import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
nums = [0] * 10000

# 모든 정렬 방법이 다 메모리 초과가 발생해서 구선생님한테 물어봄

# ⭐⭐⭐메모리를 관리해야 하는 문제⭐⭐⭐
# 1. 파이썬 내부에서 연산과 메모리를 관리하도록 하는 것이 좋다
    # https://wikidocs.net/21057
    # for문 안에 append를 하는 것보다는 list comprehension으로
    # list comprehension보다는 map() 메소드를 사용하는 것이 더 메모리 효율적
# 2. python3를 컴파일러로 선택해야 메모리가 줄어든다 (cf) 시간을 적게 해야하면 pypy3 선택하기
    # https://velog.io/@yje876/python%EB%B0%B1%EC%A4%80DP-10989-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3


# 계수 정렬 사용
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    nums[num-1] += 1

for j in range(10000):
    if nums[j] != 0:
        for k in range(nums[j]):
            print(j+1)