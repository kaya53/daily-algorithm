import sys

sys.stdin = open('input.txt')


def count_sushi(arr):
    cnt = len(set(arr))
    if c not in arr: cnt += 1
    return cnt


## 2531 회전 초밥은 통과하는데, 15961 회전 초밥은 시간 초과
for _ in range(4):
    # 접시수, 초밥 가지수, 연속해서 먹는 초밥 수, 쿠폰 번호
    n, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(n)]

    # 초기 작업
    sect = sushi[:k]
    cnt = count_sushi(sect)

    # 나올 수 있는 총 구간 n개의 크기를 갖는 배열을 만들고
    # 여기다가 각 구간이 가지는 가지수를 누적한다.
    cnt_ls = [cnt] + [0]*(n-1)

    # 0번 인덱스는 초기 작업에서 봤기 때문에 k번 인덱스부터 시작한다.
    # => 접시수와 구간의 수가 같을 때 1부터 시작하면 인덱스 에러가 남; 28번째 줄 n 자리에 8을 써서 그런 것이었음
    for i in range(k, n+k-1):
        ri = i % n  # n이 얼마가 나오건 나머지 연산자 처리를 해줘서 한바퀴 돌 수 있게 해준다.
        sect.pop(0)  # 첫번째 원소를 빼고
        sect.append(sushi[ri])  # 그 다음 원소 집어넣기
        cnt_ls[i-k+1] = count_sushi(sect)
    print(max(cnt_ls))





