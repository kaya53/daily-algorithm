# 회전 초밥(고)
import sys

sys.stdin = open('input.txt')


def code_06():
    N, d, k, c = map(int, input().split())
    belt = [int(input()) for _ in range(N)]
    sushi = [0] * (d + 1)  # 초밥 번호가 1부터 시작되기 때문에

    # 회전 초밥
    belt = belt + belt[:k - 1]

    # 쿠폰 c는 무조건 먹게됨
    cnt = 1  # 먹은 초밥의 종류 개수
    sushi[c] = 1  # 먹은 표시

    # 최초의 k개 초밥 종류
    for sushi_no in belt[:k]:
        # 처음 먹은 초밥인 경우 가짓수 증가 (똑같은 번호의 초밥을 여러 번 먹어도 1가지 먹은 것이다)
        if not sushi[sushi_no]:
            cnt += 1
        # sushi_no 초밥의 먹은 개수 증가
        sushi[sushi_no] += 1

    max_cnt = cnt
    # 슬라이딩 윈도우 반복횟수 = N-1
    # 초밥의 먹은 경험을 빼줄 위치 = i, # 더 먹을 초밥의 위치 = i + k
    for i in range(N - 1):  # i=0, 1, 2, ..., 6
        sushi[belt[i]] -= 1
        if not sushi[belt[i]]:  # 제거 : 한 번만 먹은 초밥인 경우 먹은 초밥의 가짓수 1 감소
            cnt -= 1  # A
        if not sushi[belt[i + k]]:  # 추가 :처음 먹은 초밥인 경우 가짓수 1 증가
            cnt += 1  # B
        sushi[belt[i + k]] += 1

        # A(-1), A + B(0), B(+1), X (0)

        if cnt > max_cnt:
            max_cnt = cnt

    print(max_cnt)


for _ in range(4):
    code_06()