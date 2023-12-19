# 소요시간 40분 python 412ms pypy 432ms
# 한 강의실 사용이 끝났거나, 끝난 직후에 이어서 강의실 사용 가능
# => 즉, 아직 사용이 끝난 강의실이 없으면 추가 해줘야 함
# 틀린 이유
# - 기존 강의실을 이어서 사용하는 경우 기존 강의실 정보를 heapq에서 빼주고
# 새로운 강의실 정보를 넣어줘야 한다 => 새로운 끝나는 시간 갱신
# 유의할 점
# - heapq의 첫번째 원소는 항상 최솟값이다
import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

import heapq


def solution(n, classes):
    # 빨리 시작한 순으로 소팅해야하는 이유
    # - 일단 시작한 수업이 끝나야 해당 강의실을 이용할 수 있을 지 없을 지 알 수 있음
    # - 즉, 수업이 일단 시작해야 그 끝난 시간을 보는 게 의미가 있음
    classes.sort()
    room = []
    heapq.heappush(room, classes[0][1])
    for i in range(1, n):
        s, e = classes[i]
        end = room[0]
        if end > s:  # 새로 추가해야 함
            heapq.heappush(room, e)
        else:  # 이어서 사용 가능 but 끝나는 시간을 갱신해줘야 하므로 기존 껄 빼고 넣어야 함
            heapq.heappop(room)
            heapq.heappush(room, e)
    return len(room)


# for _ in range(3):
N = int(input())
ls = [list(map(int, input().rstrip().split())) for _ in range(N)]
print(solution(N, ls))