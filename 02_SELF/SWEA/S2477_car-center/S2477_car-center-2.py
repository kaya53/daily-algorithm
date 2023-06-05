# 230605 pypy 621ms => 1시간 30분 소요
# 순서대로 천천히 처리하면 되는 문제!
# 각 창구의 우선순위에 주의해야 했다.
# heapq를 이용하면 첫번째 요소부터 작은 순대로 정렬하여 제일 작은 걸 주기 때문에 
# 이 문제에서는 사용하면 유리함
import sys
import heapq
sys.stdin = open('input.txt')


def minus_time():
    global remain, res
    
    # 접수 창구
    for i in range(1, N+1):
        if desk_recep[i] == [0, 0]: continue
        now = desk_recep[i][0]  # 현재 고객 번호
        if desk_recep[i][1]:
            desk_recep[i][1] -= 1
            if desk_recep[i][1] == 0:
                # 이 부분 문제 조건을 제대로 읽지 않아서 몇몇 테케가 틀렸었음
                # 큐에 들어온 시간, 이전에 이용한 접수 창구 번호, 고객 번호
                heapq.heappush(repair_q, (time, i, now))
                desk_recep[i] = [0, 0]
    
    # 정비 창구
    for j in range(1, M+1):
        if desk_repair[j] == [0, 0, 0]: continue
        now_p = desk_repair[j][0]  # 현재 고객 번호
        if desk_repair[j][1]:
            desk_repair[j][1] -= 1
            if desk_repair[j][1] == 0:
                remain -= 1
                if desk_repair[j][2] == A and j == B: res += now_p
                desk_repair[j] = [0, 0, 0]


def people_in():
    for no in range(1, K+1):
        if customer_time[no] == time:
            heapq.heappush(recep_q, no)


def to_reception():
    for i in range(1, N+1):
        if desk_recep[i] == [0, 0]:
            if recep_q:
                desk_recep[i] = [heapq.heappop(recep_q), recep_time[i]]
            # 더 이상 들어갈 사람이 없으면 리턴
            else: return


def to_repair():
    for j in range(1, M+1):
        if desk_repair[j] == [0, 0, 0]:
            if repair_q:
                t, recep_no, p_no= heapq.heappop(repair_q)
                desk_repair[j] = [p_no, repair_time[j], recep_no]
            else: return


T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    recep_time = [0] + list(map(int, input().split()))
    repair_time = [0] + list(map(int, input().split()))
    customer_time = [0] + list(map(int, input().split()))

    res = 0
    remain = K
    time = -1
    recep_q = []
    repair_q = []
    desk_recep = [0] + [[0, 0] for _ in range(N)]
    # 고객 번호, 남은 시간, 접수 창구 번호
    desk_repair = [0] + [[0, 0, 0] for _ in range(M)]
    while True:
        time += 1
        people_in()
        to_reception()
        to_repair()
        minus_time()
        if remain == 0: break
    print(f'#{tc} {-1 if not res else res}')