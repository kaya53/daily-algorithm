import random
import sys

sys.stdin = open('input.txt')

N = int(input())
switches = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
students = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
# print(N,switches, M, students)


def male(num):
    for i in range(N):
        if not ((i+1) % num):  # 주어진 자연수로 나누어 떨어지면
            switches[i] = int(not switches[i])  # 토글링
    return switches


def female(num):
    std = num - 1  # 인덱스가 0부터 시작하니까 1 빼주기
    s = e = std  # 시작점, 끝점 초기화
    while s >= 0 and e < N:  # 시작점 - 1, 끝점 + 1이 인덱스 범위 내일 때
        pelin_list = switches[s: e+1]
        if pelin_list == pelin_list[::-1]:  # 해당 구간이 회문이면
            s -= 1  # 다음으로 이동
            e += 1
        else:  # 범위 내여도 회문이 아닐 경우 break
            break
    # 토글링
    for idx in range(s+1, e):
        switches[idx] = int(not switches[idx])
    return switches


for sid, stu_num in students:
    if sid == 1:
        male(stu_num)  # 남학생 로직
    if sid == 2:
        female(stu_num)  # 여학생 로직

# 20개 단위로 끊어서 출력
for i in range(0, N, 20):
    print(*switches[i : i+20])