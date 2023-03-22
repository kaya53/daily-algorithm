import sys

sys.stdin = open('input.txt')

for _ in range(4):
    # 접시의 수, 초밥의 총 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
    n, d, k, c = map(int, input().split())
    belt = [int(input()) for _ in range(n)]  # 벨트에 놓인 접시 수
    #
    # # 초기 작업
    # cnt_sushi = [0] * (d+1)  # 초밥 번호가 1부터 시작하므로 개수를 하나 더 늘려준다.
    # cnt_sushi[c] = 1  # 무조건 먹을 수 있는 c번 초밥
    # for i in range(k):
    #     cnt_sushi[sushi[i]] += 1
    # cnt = d - cnt_sushi.count(0) + 1  # cnt_sushi가 d보다 1이 많기 때문에
    # res = cnt
    #
    # # 시작
    # for i in range(n):  # 모든 접시가 한 번씩 시작점이 되어주어야 하니까
    #     cnt_sushi[sushi[i]] -= 1  # 빠지는 초밥의 cnt를 빼준다
    #     if not cnt_sushi[sushi[i]] :
    #         cnt -= 1  # 지금 초밥의 카운트가 0이라는 건 방금 빠진 초밥말고는 그 초밥이 또 있지 않다는 거니까 카운트도 빼주기
    #     try:
    #         if not cnt_sushi[sushi[i+k]]: cnt += 1  # 지금 먹을 초밥이 먹었던 게 아니면 카운트 늘리기
    #         cnt_sushi[sushi[i+k]] += 1  # 해당 초밥 개수 +1
    #     except:  # try에서 인덱스 에러가 나면 여기로 오게 될 것
    #         if not cnt_sushi[sushi[i+k-n]]: cnt += 1
    #         # 내 코드에서는 에러를 처리하기 위해 계속 % 연산을 했는데
    #         # 이렇게 하면 에러가 나는 경우에만 -n을 빼서 처리해주면 됨
    #         cnt_sushi[sushi[i+k-n]] += 1
    #     if res < cnt: res = cnt
    #
    # print(res)

    # 초기 작업
    sushi = [0] * (d+1)
    sushi[c] = 1  # 쿠폰이 있으면 무조건 먹기
    max_cnt = cnt = 1  # 구간 내 초밥의 개수를 센다
    for i in range(k):
        sushi[belt[i]] += 1
        cnt += 1
        if sushi[belt[i]] > 1:
            cnt -= 1
    # print(sushi) # ok

    for i in range(n):
        ni = (i+k) % n
        # i번째는 빼고 ni번째는 넣고
        sushi[belt[i]] -= 1
        if not sushi[belt[i]]:  # 방금 빠진게 마지막 초밥이었다면 cnt 빼주기
            cnt -= 1
        sushi[belt[ni]] += 1
        if sushi[belt[ni]] == 1:  # 방금 들어온 게 첫 초밥이었다면 cnt 더해주기
            cnt += 1

        # 최대값 비교
        if max_cnt < cnt:
            max_cnt = cnt

    print(max_cnt)