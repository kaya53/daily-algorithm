# 소요 시간 25분 44ms
# 1. 20개씩 끊어 출력하기
# 2. female 함수 부분에서 s, e 변수 범위 처리
import sys

sys.stdin = open('input.txt')


def male(num):
    for s_no in range(1, S+1):
        if s_no % num == 0: switch[s_no] ^= 1


def female(num):
    s = e = num
    while s >= 1 and e <= S:
        if switch[s] != switch[e]: break
        s -= 1
        e += 1
    for i in range(s+1, e): switch[i] ^= 1


S = int(input())
switch = [-1] + list(map(int, input().split()))
N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

for k, z in students:
    if k == 1: male(z)
    elif k == 2: female(z)

# switch = switch[1:]
for r in range(1, S, 20):
    print(*switch[r: r+20])