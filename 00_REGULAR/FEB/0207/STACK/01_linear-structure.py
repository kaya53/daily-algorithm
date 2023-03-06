### 선형 자료 구조
# 1. 배열; 내부에 어떤 정보를 저장
    # - index를 이용하여 내부 값에 직접 접근
    
# 2. 스택 : Last-In, First-out(가장 마지막에 들어온 것이 제일 먼저 나간다)
    # push: 스택 안에 요소를 넣는 작업; 넣은 요소가 top이 됨
        # top의 index가 스택의 전체 길이가 됨
    # pop: 스택 밖으로 top element를 빼는 작업
    ## 하나의 요소가 그 전 요소와 연결되어서 연산이 될 때 stack을 사용할 생각을 해볼 수 있다(ex) J1141 불쾌한 날
    # 스택 사용
    # - 후위 표기된 식을 연산하여 결과 구하기 (이거 먼저 해보기)
    # - 중위 표기된 식을 입력 받아 후위 표기로 변환하는 코드 작성
    
# 3. deque(양방향 큐) : 앞에서 빼고 뒤에 넣음
    # - append, pop 연산이 압도적으로 빠름; 넣고 빼는 인덱스가 정해져 있기 때문에
    # - stack 구현에도 활용함 ; append(), pop() 활용
    # - queue: popleft(), append() 활용

from collections import deque
deq = deque()

# add element 10 to the start
deq.appendleft(10)

# add element 10 to the end
deq.append(10)

# pop element from the start
deq.popleft()

# pop element from the end
deq.pop()