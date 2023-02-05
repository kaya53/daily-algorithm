# 쉬운 거스름돈 [D2]
# 입력 : 숫자 1개 - N
# 결과저장 : 숫자 8개 - sol, 8개 item, sol = [0]*8
# 출력 : sol 출력, ' '.join(str(x) for x in sol)  // ' '.join(map(str, sol))
# sol에 값 넣기 :
# 필요한 추가적인 자료구조?
import sys
#sys.stdin = open('02_1970_input.txt')

def code_01_before():
    T = int(input())
    n = int(input())  #  test_case 별 입력은 for test_case 내부에 위치
    all_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for test_case in range(1, T + 1):
        # print 횟수를 줄일 것
        print(f"#{test_case}")
        for money in all_money:
            print(n // money, end=' ')
            n %= money
        print()


def code_01_after():
    all_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    T = int(input())
    for test_case in range(1, T + 1):
        sol = [0] * 8
        N = int(input())
        # for m in range(len(all_money)):
        #     sol[m] = (N // all_money[m])
        #     N %= all_money[m]
        for i, money in enumerate(all_money):
            sol[i] = (N // money)
            N %= money

        print(f"#{test_case}")
        print(' '.join(map(str, sol)))


def code_02_before():
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        cnt, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8 = 0, 0, 0, 0, 0, 0, 0, 0
        while N >= 10:
            cnt += N // 50000
            N = N % 50000

            cnt2 += N // 10000
            N = N % 10000

            cnt3 += N // 5000
            N = N % 5000

            cnt4 += N // 1000
            N = N % 1000

            cnt5 += N // 500
            N = N % 500

            cnt6 += N // 100
            N = N % 100

            cnt7 += N // 50
            N = N % 50

            cnt8 += N // 10
            N = N % 10

        print(f"#{i}")
        print(cnt, cnt2, cnt3, cnt4, cnt5, cnt6, cnt7, cnt8)


def code_02_after():
    all_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = 0
    T = int(input())
    # 테스트케이스 번호에 대한 target 이름 => test_case 은 어떨까요!
    for test_case in range(1, T + 1):
        sol = [0] * 8
        N = int(input())
        for i, money in enumerate(all_money):
            sol[i] = (N // money)
            N %= money
            cnt += 1

        print(f"#{test_case}")
        print(' '.join(map(str, sol)))
    print(cnt)


def code_03_after():
    # cnt = 0  # res 갱신 작업
    # cnt2 = 0 # for i 반복
    T = int(input())
    for tc in range(1, T + 1):
        money_ls = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        res = [0] * 8

        N = int(input())
        for i in range(8):
            if N == 0: break   # 400000 과 같은 경우 if N // money의 실행 횟수 감소
            money = money_ls[i]
            # cnt2 += 1
            if N // money:  # 80회 비교
                res[i] = N // money
                N %= money
                # cnt += 1   # 80회 보다 덜 수행 (그러나!  몇 번인지는 데이터에 따라 다름)

        print(f'#{tc}')
        print(*res)
    # print(f'cnt={cnt}, cnt2={cnt2}')  # cnt=44, cnt2=71


def code_04_before():
    T = int(input())
    money = [i * (10 ** j) for j in range(4, 0, -1) for i in [5, 1]]
    for i in range(1, T + 1):
        res = []  # 개수가 가변적인 경우 사용, 고정적인 개수는 [0] * 개수 사용
        price = int(input())
        for m in money:
            res.append(price // m)
            price %= m
        print(f'#{i}')
        print(*res)


def code_05_before():
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    t = int(input())
    # 개수가 고정인 경우, append는 사용하지 않는 것이 좋다
    N, result = [], []
    # testcase가 50개 이기 때문에 하나씩 입력 받고, 결과 출력이 좋다
    for _ in range(t):
        N.append(int(input()))
    # enumerate(N)을 enumerate(N, start=1)로 변경하면, idx+1 을 idx로 사용할 수 있다
    for idx, val in enumerate(N, start=1):
        #불필요한 변수는 사용하지 말자
        #left = val
        for i in moneys:
            x, val = divmod(val, i)
            result.append(x)
        print(f"#{idx}")
        # 아래의 두 줄은 print(*result) 과 같음
        print(*(i for i in result), end=' ')
        print()
        result = []


# 함수 분리시, 처리와 출력을 섞지 말자
def code_06_before():
    N = int(input())
    moneyList = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    def solve(money):
        for m in moneyList:
            print(money // m, end=' ')
            money = money % m
        print()

    for i in range(N):
        print(f'#{i + 1}')
        solve(int(input()))


def code_06_after():

    moneyList = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    def solve(money):
        sol = [0] * 8
        for i, m in enumerate(moneyList):
            sol[i] = (money // m)
            money %= m
        return sol

    T = int(input())
    for t in range(1, T+1):
        sol = solve(int(input()))
        print(f'#{t}')
        print(' '.join(map(str, sol)))

def code_07_before():
    N = int(input())
    # 입력은 한번에 하나씩 하는 것이 좋음
    money = [int(input()) for i in range(N)]
    mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i in range(N):
        sol = []   #고정 개수는  sol = [0] * 8
        for j in mon:
            # left 변수는 불필요
            res, left = divmod(money[i], j)
            money[i] = left
            sol.append(res)
        print(f'#{i + 1}')
        print(*sol)


def code_08_before():
    #  res = [0] * 8 이 빠름
    res = [0 for _ in range(8)]
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    t = int(input())
    for t1 in range(t):
        N = int(input())
        for i in range(8):
            # a, b 변수는 불필요
            a, b = divmod(N, lst[i])
            res[i] = a
            N = b
        print(f"#{t1 + 1}")
        print(*res)

def code_09_before():
    S = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    t = int(input())

    # test_case 번호를 range(1, t+1) 로 해결할 것
    cnt = 1
    # for 문 속에서 test_case마다 새롭게 생성이 안전함 (현 문제에서는 문제 없음)
    sol = [0] * 8
    for _ in range(t):
        N = int(input())
        # for문에서 in 뒤는 1회 수행되므로 복잡해도 OK, for문 블록 내부는 단순한 것이 좋음
        for x in range(8):
            sol[x] = N // S[x]
            N = N - (sol[x] * S[x])
        print('#' + str(cnt))
        print(' '.join(map(str, sol)))
        cnt += 1

##  조심 (iterator, iterable), iterator 는 iterable 이라고 할 수 있음
def code_10_before():
    # list로 변환하는 작업은 필요 없음
    sol = [0] * 8
    print(" ".join(list(map(str, sol))))

def code_0x_before():
    t = int(input())
    sol = [0] * 8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # range를 ...  안쓰묜  두 번 반복하게 됨   (1, t + 1) 는 tuple
    for i in (1, t + 1):
        n = int(input())
        for j in range(len(money)):
            sol[j] = n // money[j]
            n -= money[j] * sol[j]
        print(f'#{i}')
        print(*sol)

code_0x_before()