import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):  # 연산을 할거면 여기서 해주는 게 낫다; 아래 출력에서 tc+1을 하면 계속 연산을 하게 됨
    n, q = map(int, input().split())  # 상자 개수, 상자를 바꾸는 횟수
    arr = [0] + [list(map(int, input().split())) for _ in range(q)]  # 상자를 바꾸는 작업
    boxes = [0] * n  # 상자 초기 상태

    for i in range(1, q+1):
        l, r = arr[i]
        boxes[l-1:r] = [i] * (r-l+1)  # 슬라이싱도 내부적으로는 반복을 돈다

    print(f'#{tc}', ' '.join(map(str, boxes)))

# # 테케 만들기
# print(100, 100)
# for i in range(1, 100):
#     print(i, i+1)