# 소요시간 30분 pypy 423ms python 556ms
# 학생 간의 중복을 체크해야 함!
import sys

sys.stdin = open('input.txt')


def solution(n, arr):
    cnt = [set() for _ in range(n)]
    for j in range(5):
        for i1 in range(n):
            for i2 in range(i1+1, n):
                if arr[i1][j] == arr[i2][j]:
                    cnt[i2].add(i1)
                    cnt[i1].add(i2)

    student = 0
    mmax = 0
    for k in range(n):
        s = cnt[k]
        if mmax < len(s):
            mmax = len(s)
            student = k
    return student+1


# for _ in range(3):
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, arr))