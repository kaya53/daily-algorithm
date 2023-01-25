import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())  # 문서의 총 개수, 궁금한 문서의 현 위치
    arr = list(map(int, sys.stdin.readline().rstrip().split()))  # 문서들의 중요도
    copies = deque(enumerate(arr))  # enumerate(arr)을 이용해 큐를 만든다

    res = []
    while copies:
        first = copies.popleft()  # 비교를 할 첫 원소를 꺼낸다.
        for i in range(len(copies)):  
            # 꺼냈으니까 copies의 원소는 하나 줄어들어서 range(1, len(copies)+1) 이렇게 할 필요가 없다.
            if first[1] < copies[i][1]:  # 꺼낸 문서의 중요도와 copies 내의 문서의 중요도 비교
                copies.append(first)  # 하나라도 큰게 있으면 무조건 맨 뒤로 보내고
                break  # for문 끝내기 -> for문이 끝나면 continue를 안써도 while문의 다음 반복으로 감
        else:  # 꺼낸 원소가 제일 클 때
            res.append(first)  # 결과값을 담는 배열에 차례대로 쌓아 넣는다
        # continue  # 어차피 이 이후에 while문 내에 실행시킬 코드가 없으므로 안써도 됨

    # 출력하기
    for i in range(len(res)):  
        if res[i][0] == M:  # 0번 인덱스: 원래 순서
            print(i+1)  # i+1 : 프린터 큐에 따라 인쇄되는 순서