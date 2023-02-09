## power set
# 집합이 주어지고 이 집합의 원소들을 선택하여 가능한 모든 부분 집합을 생성한 것
# {a, b, c}
    # 각각 원소는 부분집합에 들어가거나 안들어가거나
    # 이걸 중심으로 생각해야 함
# 원소가 n개인 집합의 파워셋 -> nC0 + nC1 + nC2 +....+nCn = 2**n
# 그래서 n의 최대 개수를 잘 보고 결정해야 함
# j1127 맛있는 음식 문제는 최대 n이 10이므로(2**10=1024) 쓸 수 있음
    # ⭐⭐⭐ but n이 크면 적절치 않음 ⭐⭐⭐
    # (cf) 2**20 : 약 100만, 2**30 : 약 10억

# 중심 로직
n = int(input())  # 집합 원소의 개수
numbers = list(map(int, input().split()))  # 집합의 원소들
is_selected = [False] * n
# 배열의 개수를 고정할 수 있다면 고정된 배열에 넣었다 빼는 게 성능 상 더 유리함 ; append, pop하는 게 좋지는 않음
def subset(idx):
    ## 종료 조건 - 원소 n개에 대해서 넣을 지, 말 지를 모두 고려했을 때
    if idx == n:
        for i, elem in enumerate(is_selected):
            print(str(numbers[i]) if elem else 'X', end='\t')
        print()
        return
    
    ## 가지치기가 항상 효율적인 건 아님 - 이것도 연산이 이루어지기 때문에 잘 따져보고 해야 함
    
    ## 재귀 유도 부분
    # 부분 집합 구성에 원소를 넣기
    is_selected[idx] = True
    # 다음 원소로 넘어가기 - 나를 선택한 채로 뒤에서 할 수 있는 걸 다하고 돌아온 지점
    subset(idx+1)
    # 부분 집합 구성에 원소를 넣지 않기
    is_selected[idx] = False
    # 다음 원소로 넘어가기 - 나를 선택하지 않은 채로 뒤에서 할 수 있는 걸 다하고 돌아온 지점
    subset(idx + 1)


subset(0)
#   1	4	6
#   1	4	X
#   1	X	6
#   1	X	X
#   X	4	6
#   X	4	X
#   X	X	6
#   X	X	X
