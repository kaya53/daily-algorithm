n = 10
numbers= list(range(1, 11))
is_selected = [False] * n
def subset(idx):
    if idx == n:
        for i, elem in enumerate(is_selected):
            print(str(numbers[i]) if elem else '0', end=' ')
        print()
        return
    ## 재귀 유도 부분
    # 부분 집합 구성에 원소를 넣기
    is_selected[idx] = True
    # 다음 원소로 넘어가기 - 나를 선택한 채로 뒤에서 할 수 있는 걸 다하고 돌아온 지점
    subset(idx + 1)
    # 부분 집합 구성에 원소를 넣지 않기
    is_selected[idx] = False
    # 다음 원소로 넘어가기 - 나를 선택하지 않은 채로 뒤에서 할 수 있는 걸 다하고 돌아온 지점
    subset(idx + 1)

subset(0)