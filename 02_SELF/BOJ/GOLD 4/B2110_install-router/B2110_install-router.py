# 이진 탐색
# - 출력하는 값을 이진 탐색으로 찾는다고 생각하자
# => 여기서는 집 간의 거리
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
nums = [int(input()) for _ in range(N)]
nums.sort()

start = 1
end = nums[-1]-nums[0]
res = 0
while start <= end:
    mid = (start+end) // 2
    curr = nums[0]
    cnt = 1  # 설치한 공유기 수
    for i in range(1, N):  # 공유기 놓기
        if nums[i] - curr >= mid:  # 가장 인접한 거니까 같거나 큰 경우만
            cnt += 1
            curr = nums[i]  # 설치 후 다음 공유기 보러

    if cnt >= C:  # 같은 수거나 더 많이 설치 => 거리를 더 늘릴 여지가 있음
        res = mid  # cnt == C인 경우에 갱신되도록
        start = mid + 1  # 큰 거리로 가기
        # print('s', start)
    else:  # 거리를 줄여야 함
        end = mid - 1
        # print('e', end)
print(res)