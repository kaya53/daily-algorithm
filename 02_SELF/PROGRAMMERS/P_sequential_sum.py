def two_pointer(n, k, accum):
    left = right = 0
    answer = [1000000, 1000000]

    while left < n and right < n:
        tot = accum[right]
        if left: tot = accum[right] - accum[left - 1]

        if tot > k: left += 1
        elif tot < k: right += 1
        elif tot < k: right += 1
        else:
            # print(left, right)
            if answer[0] == 1000000:  # 갱신된적 x
                answer = [left, right]
            else:  # 갱신된적 ㅇ
                d = answer[1] - answer[0] + 1
                if d > right - left + 1:
                    answer = [left, right]
                elif d == right - left + 1 and answer[0] > left:
                    answer = [left, right]
                left += 1  # 같으면 언제나 1 늘려주기
    return answer


def solution(sequence, k):
    n = len(sequence)
    # sequence가 오름차순 수열이기에 가능한 코드
    accum = [0] * n
    accum[0] = sequence[0]
    for i in range(1, n):
        accum[i] = accum[i - 1] + sequence[i]

    return two_pointer(n, k, accum)