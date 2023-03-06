import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    # cnt_ls = [0] * 101  # 카드 숫자는 0부터 9까지니까 10까지만 해도 됨
    cnt_ls = [0] * 10

    # cards를 반복의 용도로 쓰기 때문에 그냥 map으로 해서 돌려도 된다
    for card in cards:
        cnt_ls[card] += 1
    # print(cnt_ls)

    max_cnt = max_card = 0  # 나올 수 있는 최소값
    for i, cnt in enumerate(cnt_ls):
        # =도 넣어서 장수가 같아도 가장 큰 수가 max_card가 되도록 했다
        # if cnt != 0 and cnt >= max_cnt:  # cnt !=0 대신 cnt라고 써도 됨
        if cnt and cnt >= max_cnt:
            max_cnt = cnt
            max_card = i
    
    print(f'#{tc} {max_card} {max_cnt}')