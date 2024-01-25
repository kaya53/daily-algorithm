# python 44ms: 의미 없음
# - 이분 탐색의 기준: 두 휴게소 사이의 거리
# - 두 휴게소 사이의 거리가 mid일 때 몇 개의 휴게소를 지을 수 있는 지
import sys

sys.stdin = open('input.txt')


def solution(n, m, l, rest):
    rest.sort()
    rest = [0] + rest + [l] # l-1 => l로 고침
    left = 1  # 0 => 1로 고침; 끝에 못세운다는 의미는 시작점에도 못세운다는 의미!
    right = l-1

    answer = 0
    while left <= right:
        mid = (left+right) // 2
        cnt = 0
        for i in range(1, len(rest)):
            if rest[i] - rest[i-1] > mid:
                cnt += (rest[i] - rest[i-1] - 1) // mid
        if cnt <= m:
            answer = mid
            right = mid - 1
        elif cnt > m:
            left = mid + 1
    return answer


# for _ in range(4):
N, M, L = map(int, input().split())
arr = []
if N: arr = list(map(int, input().split()))
print(solution(N,M,L,arr))