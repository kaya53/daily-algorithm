import sys

sys.stdin = open('input.txt')

for _ in range(8):
    N = int(input())  # 총 과목 수
    arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 현재 성적

    # 성적 최대값 구하기
    mmax = 0
    for num in arr:
        if num > mmax:
            mmax = num
    # print(max(arr), mmax)

    # 조작된 점수들의 합 구하기
    ssum = 0
    for num in arr:
        ssum += (num / mmax)*100

    print(ssum / N)