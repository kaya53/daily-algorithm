from heapq import heappush, heappop


def solution(n, k, enemy):
    answer = 0
    # 무적권으로 다 막을 수 있음
    if len(enemy) <= k: return len(enemy)

    hq = []
    for i, v in enumerate(enemy):
        heappush(hq, -v)  # 최대 힙
        n -= v
        if n < 0:  # 무적권을 써야 할 때
            if k > 0:  # 무적권 사용 가능
                use = -heappop(hq)  # 가장 강한 적을 꺼낸다
                n += use  # 그 적에 대해 무적권 사용
                k -= 1
                answer = i + 1
            else:  # 사용 불가
                answer = i
                break
        else:  # 다음으로 넘김
            answer = i + 1
        # print('현재 값: ', v, '무적권 횟수: ', k, '남은 병사 수: ', n)

    return answer
