import sys

sys.stdin = open('input.txt')


# 통과 코드
for _ in range(3):
    A, B, V = map(int, input().split())
    # print(V-A)
    left = V - A
    day = A - B  # 달팽이가 하루에 움직이는 거리
    cnt = 1  # 정상에 도달한 그 마지막 날
    if not (left % day):  # 남은 거리와 달팽이가 하루에 움직이는 거리가 나누어 떨어지면 그만큼만 더하고
        cnt += left // day
    if left % day > 0:  # 나누어 떨어지지 않으면 내일 낮동안 또 올라가야 하니까 1 더해주기
        cnt += left // day + 1

    print(cnt)

# for _ in range(3):
#     A, B, V = map(int, input().split())
#     # print(V-A)
#     res = V - A
#     day = A - B  # 달팽이가 하루에 움직이는 거리
#     cnt = 1  # 정상에 도달한 그 마지막 날
#     # while res > 0:
#     # res -= A - B  # 올라가고 미끄러지는 날들
#     if day > res:  # 하루에 올라갈 수 있는 거리가 남은 거리보다 크면
#         cnt = 2
#     else:  # 그렇지 않으면 며칠에 걸쳐 영차영차
#         cnt = res // (A - B) + 1
#
#     print(cnt)