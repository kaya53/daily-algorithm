### 비선형 구조
# https://colab.research.google.com/drive/1HCK7xxwfhjJi-6QvXizIJQaDGRd-hq1l#scrollTo=LH0GkhrBidFm
## 데이터를 저장하는 구조
# 1. 배열 : 연속된 메모리에 저장됨 ; 인덱스로 주소를 계산해서 직접 접근할 수 있음
    # - 따라서 크기를 할당해 놓는 것이 좋음
    # - 크기를 할당해 놓지 않고 append, pop 등을 하면 메모리 확장이나 재할당이 일어날 수 있음

# 2. 연결 리스트 : 불연속한 메모리를 서로 연결해서 쓰는 배열
    # - 단일 연결보다는 다중 연결하는 연결 리스트를 더 많이씀
    # - 단일 연결: 그 위치까지 갈 때, 연결이 끊어졌을 때 위험성이 있음
    # - 장점: front, rear에 접근하는 것은 쉬움
    # - 단점: 중간 부분에 바로 접근하고 싶을 때는 불리함
        # - 연결 리스트 내에 모든 값의 주소를 저장해 놓은 것이 아니라 front, rear 주소만 저장해놓고 연결 상태를 보는 형태이기 때문
    
    # 이걸 활용한 것이 트리, 그래프 개념


## 데이터를 활용하는 구조
# 운영체제 내부 파일 관리 구조: 트리 구조
# 1. 선형 구조: 배열, 큐, 스택, deque
    # - 스택: 포함 구조가 나올 때 유리함
    # - 처음 게 열리고, 그 다음 게 열리고, ... 가장 마지막 것이 닫히면 앞의 것들도 순차적으로 닫히기 시작하는 것들
        # - (ex) 재귀
        
# 2. 비선형 구조
    # - 탐색, 관계 표현에 주로 활용
    # - graph, tree 등
    # - 트리: 계층을 가짐 -> 노드 간에 순환을 하지 않음
    # - 그래프 : 계층이 따로 존재하지 않음