import sys

sys.stdin = open('input.txt')


def solution(n, l, pools):
    answer = 0

    pools.sort()
    last = 0  # 마지막 널빤지 위치
    for s, e in pools:
        if last > e: continue
        for now in range(s, e):
            if last > now: continue  # 놓을 필요 없음
            answer += 1
            if last <= s:
                last = s+l
            else:  # 웅덩이 일부에 이미 널빤지가 있음
                last += l
            # print('마지막 널판지', last, '사용한 널판지', answer)
    return answer


N, L = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
print(solution(N, L, arr))