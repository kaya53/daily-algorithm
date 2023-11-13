# 소요시간 13분 pypy 112ms python 48ms
# 진우의 달 여행과 유사
import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def solution():
    n = int(input().rstrip())
    # r 비용, g 비용, b 비용
    dist = [[0, 0, 0] for _ in range(n)]
    dist[0] = list(map(int, input().rstrip().split()))

    for i in range(1, n):
        # i번째 집에서 드는 비용
        r, g, b = map(int, input().split())
        br, bg, bb = dist[i-1]  # 이전 집까지의 최소 비용
        dist[i] = [min(bg, bb)+r, min(br, bb)+g, min(br, bg)+b]

    return min(dist[-1])


# for _ in range(5):
print(solution())