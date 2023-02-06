import sys

sys.stdin = open('input.txt')

for _ in range(4):
    # 접시의 수, 초밥의 총 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
    n, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(n)]

    # 초기 작업
    cnt_sushi = [0] * (d+1)  # 초밥 번호가 1부터 시작하므로 개수를 하나 더 늘려준다.
    cnt_sushi[c] = 1  # 무조건 먹을 수 있는 c번 초밥
    for i in range(k):
        cnt_sushi[sushi[i]] += 1
    cnt = d - cnt_sushi.count(0) + 1  # cnt_sushi가 d보다 1이 많기 때문에
    res = cnt

    # 시작
    for i in range(n):  # 모든 접시가 한 번씩 시작점이 되어주어야 하니까
        cnt_sushi[sushi[i]] -= 1  # 빠지는 초밥의 cnt를 빼준다
        if not cnt_sushi[sushi[i]] :
            cnt -= 1  # 지금 초밥의 카운트가 0이라는 건 방금 빠진 초밥말고는 그 초밥이 또 있지 않다는 거니까 카운트도 빼주기
        try:
            if not cnt_sushi[sushi[i+k]]: cnt += 1  # 지금 먹을 초밥이 먹었던 게 아니면 카운트 늘리기
            cnt_sushi[sushi[i+k]] += 1  # 해당 초밥 개수 +1
        except:  # try에서 인덱스 에러가 나면 여기로 오게 될 것
            if not cnt_sushi[sushi[i+k-n]]: cnt += 1
            # 내 코드에서는 에러를 처리하기 위해 계속 % 연산을 했는데
            # 이렇게 하면 에러가 나는 경우에만 -n을 빼서 처리해주면 됨
            cnt_sushi[sushi[i+k-n]] += 1
        if res < cnt: res = cnt

    print(res)