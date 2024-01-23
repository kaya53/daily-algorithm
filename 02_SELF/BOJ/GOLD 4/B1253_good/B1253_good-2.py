import sys

sys.stdin = open('input.txt')


def binary_search(i, n, target, nums):
    left = 0 if i else 1
    right = n - 1
    while left < right:
        # 다른 두 수의 합을 봐야하기 때문
        # 자기 자신과 같은 경우, 두 수가 같은 경우 제외
        # 이 세 줄을 여기 넣으니까 맞았고 아래로 옮기니까 틀렸음
        if left == i: left += 1
        if right == i: right -= 1
        if left == right: continue
        
        tot = nums[left] + nums[right]
        if tot == target:
            return 1
        elif tot < target: # 더한게 타겟보다 작음
            left += 1
        else:
            right -= 1
    return 0


def solution(n, nums):
    answer = 0
    nums.sort()
    for i in range(n):
        num = nums[i]
        answer += binary_search(i, n, num, nums)
    return answer


for _ in range(2):
    print(solution(int(input()), list(map(int, input().split()))))
