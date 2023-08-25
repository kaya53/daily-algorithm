# 소요시간: 15분
# 아이디어가 필요한 브론즈 문제
# => 한 명이 들어갈 수 있는 최소 단위를 자르고
# 그 단위가 전체에 몇 번 들어갈 수 있는 지 찾자
import sys

sys.stdin = open('input.txt')

H, W, N, M = map(int, input().split())  # 전체 행, 열 / 띄어앉아야 할 행, 열 길이(or 관계)

# 가로에 들어갈 수 있는 최대 인원
k, v = divmod(W, M+1)
if v: k += 1

# 세로에 들어갈 수 있는 최대 인원
x, z = divmod(H, N+1)
if z: x += 1

print(k*x)