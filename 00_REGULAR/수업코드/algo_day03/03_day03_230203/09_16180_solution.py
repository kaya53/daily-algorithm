import sys
sys.stdin = open('09_16180_input.txt')

def code_01():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        # cards 를 한 번 scan 하고 다시 사용하지  않는다면 list로 바꿀 필요 없음
        cards = list(map(int, input()))  # [4,9,6,7,9], 최대 100장, 0 ~ 9 범위의 숫자
        #cnt_ls = [0] * 101  # 왜 101 이죠??  낭비
        cnt_ls = [0] * 10    # 숫자 범위가 0 ~ 9 이기 때문에

        for card in cards:
            cnt_ls[card] += 1

        max_cnt = max_card = 0  # 나올 수 있는 최소값
        for i, cnt in enumerate(cnt_ls):
            # =도 넣어서 장수가 같아도 가장 큰 수가 max_card가 되도록 했다
            #if cnt != 0 and cnt >= max_cnt:
            if cnt and cnt >= max_cnt:
                max_cnt = cnt
                max_card = i

        print(f'#{tc} {max_card} {max_cnt}')

def code_02():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        # list(input().strip()) -> input().strip()
        # list(map( ...)) -> map(...)
        cards = list(map(int, list(input().strip())))

        card_cnt = [0] * 10
        for c in cards:
            card_cnt[c] += 1

        max_cnt, max_card = 0, -1
        # range는 (start, stop, step), 이 때 stop은 포함되지 않음, 0은 비교대상이 아님 (조심)
        # for c in range(9, 0, -1): 을 사용하면  0을 비교하지 못함!!
        for c in range(9, -1, -1):
            if card_cnt[c] > max_cnt:
                max_cnt, max_card = card_cnt[c], c
        print(f'#{tc} {max_card} {max_cnt}')


def code_03():
    t = int(input())
    for test_case in range(1, t + 1):
        int(input())  # 입력 받은 뒤 사용하지 않고 버림  :  이런 경우 int 변환은 하지 말 것
        a = input()
        d = {}
        for i in a:
            d.setdefault(i, 0)
            d[i] += 1
            # sorted() => O(NlogN), 필요시 1회 사용, for 문 속에서 의미없이 사용 금지
            # d.items()를 2차 정렬, value순 오름차순, value가 같을 때는 key순 오름차순
            d2 = sorted(d.items(), key=lambda x: (x[1], x[0]))
            print(d2)
        print(f'#{test_case}', ' '.join(map(str, d2[-1])))


# 라이브러리 사용하지 마세용
def code_04():
    # 숫자카드
    from collections import Counter
    T = int(input())
    for test_case in range(T):
        a = int(input())
        #  reversed(sorted(input())) => sorted(input(), reverse=True)
        re_s = reversed(sorted(input()))
        result = Counter(re_s)
        real_result = result.most_common(1)
        print(real_result)
        print(f"#{test_case + 1} {' '.join(map(str, *real_result))}")

def code_05():
    T = int(input())

    for test_case in range(1, T + 1):
        n = int(input())
        result = [0] * 10
        n_list = map(int, input())

        for i in n_list:
            result[i] += 1

        max_val, max_idx = -1, -1
        for i in range(len(result)):
            if result[i] >= max_val:
                max_idx, max_val = i, result[i]

        print(f"#{test_case} {max_idx} {max_val}")

#  로직이 안좋음, .count(), .index(), max(), sum() -> O(N)
def code_06():
    T = int(input())
    for test_case in range(1, T + 1):
        n = int(input())
        card = input()

        cnt_lst = []
        for i in card:
            a = list(card).count(i)
            cnt_lst.append(a)

        if sum(cnt_lst) == len(cnt_lst):
            print(f'#{test_case} {max(list(card))} {max(cnt_lst)}')
        else:
            print(f'#{test_case} {card[cnt_lst.index(max(cnt_lst))]} {max(cnt_lst)}')

def code_07():

    for t in range(1, int(input()) + 1):
        # dic = {}
        # for i in range(10):
        #     dic[i] = 0
        dic = dict.fromkeys(range(10), 0)

        input()
        graph = input()
        for i in graph:
            dic[int(i)] += 1

        a = max(dic.values())
        print(f"#{t}", *(max((k, v) for k, v in dic.items() if a == v)))

def code_08():
    T = int(input())
    for case in range(1, T + 1):
        # 카드 개수 입력
        cards = int(input())
        card = [0] * 10

        # 숫자별 카드 장 수 세기
        for j in map(int, input()):
            card[j] += 1

        # 숫자와 최대 장 수 구하기
        maxx = card[0]
        max_idx = 0
        for idx, k in enumerate(card):
            if maxx <= k:
                maxx = k
                max_idx = idx

        print(f'#{case} {max_idx} {maxx}')

def code_09():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        #
        lst = list(map(int, input()))   # 0 1 3 6 2 3 2 8

        std = sorted(set(lst))  # std = [0, 1, 2, 3, 6, 8]
        arr = []
        for x in std:
            arr.append(lst.count(x))  # arr = [1 1 2 2 1 1]
        arr = sorted(arr)  # arr = [1 1 1 1 2 2]

        if arr.count(max(arr)) == 1:
            print(f"#{test_case}", std[arr.index(max(arr))], max(arr))
        else:
            print(f"#{test_case}", std[-1], arr[-1])

def code_10():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())
        cards = int(input())  # 파이썬은 무한 정수이기 때문에 100자리 정수 가능
        cards_count = dict.fromkeys(range(10), 0)

        while cards != 0:
            cards, m = divmod(cards, 10)
            cards_count[m] += 1
        # max(cards_count.values()) => 10번 반복할 이유가 없음.  (code_07 함수처럼 변수사용)
        li = sorted([(k, v) for k, v in cards_count.items() if max(cards_count.values()) == v], reverse=True)
        card, cnt = li[0]

        print(f'#{test_case}', card, cnt)


