import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 선택 정렬