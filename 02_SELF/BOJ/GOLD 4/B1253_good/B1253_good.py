# 소요시간: 의미 없음 pypy 176ms
# => 투 포인터
# - 문제에서 다른 수 두개의 합으로 나타낼 수 있는 수의 개수를 구하라고 함
# - 수의 위치(인덱스)가 다르면 값이 같아도 다른 수
# => 답을 구할 때 각 수를 좋은 수 후보로 두고 좋은 수가 될 수 있나 없나를 봐야 함
import sys

sys.stdin = open('input.txt')

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i in range(N):  # 음수로 시작할 수도 있기 때문에 2부터 시작하면 안됨
    now_res = nums[i]  # 좋은 수 후보
    left, right = 0, N-1
    while left < right:
        if left == i: left += 1
        elif right == i: right -= 1
        if left == right: continue
        tot = nums[left] + nums[right]

        if tot == now_res:
            cnt += 1
            break  # 다음 후보로
        elif tot < now_res: left += 1
        elif tot > now_res: right -= 1
print(cnt)