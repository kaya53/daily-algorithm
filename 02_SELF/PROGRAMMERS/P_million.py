def solution(e, starts):
    cnt = [1] * (e + 1)

    # 이것도 어느 정도 시간이 소요되는 데 s, e 사이를 봐야 함
    for i in range(2, e + 1):  # 단 수
        for x in range(i ** 2, e + 1, i):
            if x == i ** 2 and i ** 2 <= e:
                cnt[i ** 2] += 1
            else:
                cnt[x] += 2

    # 10만 개에 대해서 하기
    max_ls = [0] * (e + 1)
    max_ls[-1] = e
    for j in range(e - 1, min(starts) - 1, -1):
        if cnt[max_ls[j + 1]] <= cnt[j]:
            max_ls[j] = j
        else:
            #
            max_ls[j] = max_ls[j + 1]

    return [max_ls[s] for s in starts]
