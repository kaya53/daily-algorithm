### 재귀 함수
# 함수 속에서 자기 자신을 호출하는 것
# (모든)함수의 로컬 변수 - 스택 메모리를 사용한다
    # -> 그래서 재귀 함수의 리턴값들도 스택의 형태로 사용된다
# - 재귀 깊이가 너무 깊으면 RecursionError 발생
    # - 함수에 parameter의 개수가 많으면 안됨 -> 많으면 가능한 재귀 깊이가 좀 얕아짐
    # - parameter 하나가 하나의 주소이기 때문에 그렇다
# - 종료 조건을 함수 내 어느 위치에 쓰느냐에 따라 호출 횟수가 줄어들 수 있다
    # - 호출문 전에 작성해야 재귀가 적절한 때에 멈춤
# - 함수의 역할/기능을 명확히 아는 것이 가장 중요함
# - 재귀가 반복을 대신 해주기 때문에 재귀 안에서 실행할 것은 for/while문 내부에 있는 것


arr = []
def func(cnt):
    if cnt == 10:
        return arr
    # a = list(range(100))
    # print(cnt, len(a))
    arr.append(cnt)
    func(cnt+1)
    return arr

# print(func(0))

# [Previous line repeated 1285 more times]
# RecursionError: maximum recursion depth exceeded


## 1. 재귀 함수를 언제 멈출까? - 함수의 종료: return하면 종료된다

# 1 2 3 4 5 출력하고 멈추기
# 출력하고 return 없는 재귀
def func_04(num):
    if num > 5:  # 종료조건
        return
    print(num, end=' ')
    func_04(num + 1)

# func_04(1)  # return이 없으므로 print를 쓰면 None도 같이 출력된다


# arr을 가지고 다니는 재귀
# python은 함수에 리스트를 넣으면 전역처럼 리스트를 다룬다
# 함수의 파라미터는 각각 하나의 객체이다 -> n개의 파라미터이면 n개의 주소를 가지고 있는 것이다.
# 그래서 아래처럼 return func_05(num+1, arr) 처럼 하면 같은 주소를 가진 객체를 넘기는 것이므로
# 전역 변수처럼 같은 주소의 값이 변하는 것이다.
# 그래서 내가 하고 싶은 단계마다 arr이 변하도록 하려면 단계마다 arr이 다른 주소를 가지게 해야 한다.
    # 강사님이 이렇게 하고 싶으면 arr.copy()해서 재귀를 하라고 하셨는데
    # 내가 전에 봤던 visited를 가지고 다니는 코드는 뭔가 이렇게 한게 아닌 것 같다 -> 그 때 가서 다시 보자
# 더하기, 곱하기 연산자는 새로운 객체를 만들어 낸다
# append, insert, pop같은 연산은 기존의 객체에서 삭제, 추가를 하는 것이다

# 그래서 아래처럼 짜면 func_06과 같은 결과가 나옴
def func_05(num, arr):
    if num > 5:
        return arr
    arr.append(num)
    return func_05(num+1, arr)

# print(func_05(1, []))


# arr을 전역으로 뺀 재귀
arr = []
def func_06(num):
    if num > 5:
        return arr
    arr.append(num)
    return func_06(num+1)

# print(func_06(1))


# 5 4 3 2 1 출력하기
# func_07 : cnt를 역순으로 출력하는 함수
def func_07(cnt):
    if cnt > 5:
        return
    func_07(cnt + 1)
    print(cnt)

    # 이렇게 하면 5 4 3 2 출력됨 -> 최초 입력값이 0이면 이렇게 해야 함
    # if cnt == 5:
    #     return cnt
    # res = func_07(cnt + 1)
    # print(res)
    # return cnt

# func_07(1)


# 1 2 3 4 5 5 4 3 2 1 출력하기
def func_08(cnt):
    if cnt > 5:
        return
    print(cnt)
    func_08(cnt + 1)
    print(cnt)
func_08(1)


# 1 2 3 4 5 4 3 2 1 출력하기
def func_09_my(cnt):
    # 내 풀이
    if cnt == 5:
        print(cnt, end=' ')
        return
    print(cnt, end=' ')
    func_09_my(cnt+1)
    print(cnt, end=' ')

def func_09_tr(cnt):
    # 강사님 풀이
    print(cnt, end=' ')
    if cnt == 5:
        return
    func_09_tr(cnt+1)
    print(cnt, end=' ')

print('0909')
func_09_my(1)
print()
print('----------')
func_09_tr(1)
print()

print('-----------10------------')
## 1 3 6 10 15 출력 시키기; 계차 수열
N = 5
depth1 = depth2 = 0
def func_10_print(cnt, prev_sum):  # 프린트문 사용
    global depth1
    depth1 +=1
    if cnt > N:
        print(prev_sum)
        return
    prev_sum += cnt
    func_10_print(cnt+1, prev_sum)


def func_10_return(cnt):  # 리턴 사용
    global depth2
    depth2 += 1
    if cnt == N:
        return cnt
    res = func_10_return(cnt+1)
    res += cnt
    return res

# func_10(1, 0)
func_10_print(1, 0)
print(func_10_return(1))
print(depth1, depth2)


def tree(cnt, N):
    if cnt > N: return
    # print(cnt)  # 전위 순회 (루트 - 왼 - 오 )
    tree(cnt+1, N)
    print(cnt)  # 중위 순회 (왼 - 루트 - 오 )
    tree(cnt+1, N)
    # print(cnt)  # 후위 순회 (왼 - 오 - 루트)

print('--------tree-------------')
tree(1, 3)