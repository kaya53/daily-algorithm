import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt')


def binary_search(x, m, location):
    left = 0
    right = m-1
    while left <= right:
        mid = (left+right)//2
        if x <= location[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right


def solution(m, n, l, location, animals):
    location.sort()

    cnt = 0
    for x, y in animals:
        near = binary_search(x, m, location)

        if near < m-1 and abs(location[near] - x) > abs(location[near+1]-x):
            near += 1
        near = location[near]
        dist = abs(x-near) + y
        if dist <= l:
            cnt += 1
    return cnt


# for _ in range(2):
M, N, L = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
nums = [tuple(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(M, N, L, arr, nums))