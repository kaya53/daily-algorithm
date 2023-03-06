import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

for tc in range(1, 11):
    N = int(input())  # 총 건물 수
    buildings = list(map(int, input().split()))

    cnt = 0
    for i in range(2, N-2):
        max_neighbor = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if max_neighbor < buildings[i]:
            cnt += buildings[i] - max_neighbor
    print(f'#{tc} {cnt}')