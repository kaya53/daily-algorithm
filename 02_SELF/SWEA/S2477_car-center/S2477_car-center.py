import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):

    N, M, K, A, B = map(int, input().split())  # 접수 창구 개수, 정비 창구 개수, 방문 고객 수, 지갑 두고 간 사람이 방문한 접수/ 정비 창구 번호(
    reception_time = list(map(int, input().split()))  # 접수 창구 걸리는 시간 list
    repair_time = list(map(int, input().split()))  # 정비 창구 걸리는 시간 list
    visitor_time = list(map(int, input().split()))  # 각 고객이 정비소를 방문한 시간 list
    visitor_no = 0  # 0번 인덱스부터 시작
    visitors = len(visitor_time)

    # 방문 기록 저장 배열; index = 고객 번호, [접수, 정비]
    # 고객 번호가 0부터 시작이니까(인덱스 상) -1을 기본값으로 함
    visitor_info = [[-1, -1] for _ in range(K)]

    # 접수 창구, 정비 창구
    # default = -1, 누군가 있다면 [고객번호, 시간]
    reception = [-1] * N
    repair = [-1] * M

    # 각 창구의 대기줄
    reception_wait = []
    repair_wait = []

    time = 0

    # 순서: 접수 창구 -> 정비 창구
    # 빈 접수 창구나 빈 정비 창구가 없으면 생길 때까지 기다리기
    # 접수 창구 우선순위
    # 1. 고객 번호가 낮은 순
    # 2. 빈 창구가 여러 곳이면 접수 창구번호 낮은 곳부터
    # 정비 창구 우선 순위
    # 1. 먼저 기다리고 있는 고객 먼저
    # 2. 두 명 이상의 고객이 동시에 접수를 완료하고 왔다면, 이용한 접수 창구 번호가 작은 순서
    # 3. 빈 창구가 여러 곳이면 정비 창구 번호가 낮은 곳 부터

    flag = True
    while flag:
        # 0. 정비 창구에서 볼일 다 본 사람 out
        for i in range(M):
            if repair[i] != -1 and repair[i][1] == 0:
                repair[i] = -1
        # 1. 접수에서 볼일 다 본 사람 '정비 대기줄'로 옮기기
        for i in range(N):
            if reception[i] != -1 and reception[i][1] == 0:
                repair_wait.append(reception[i][0])
                reception[i] = -1

        # 2. 현재 시간에 들어온 고객을 접수 줄로
        for i in range(visitor_no, visitors):
            # i번째 사람이 온 시간 == 현재 시간이면
            if visitor_time[i] == time:
                # 접수 줄로
                reception_wait.append(i)
            else:
                visitor_no = i
                break  # 한 명 찾으면 끝내야 하니까

        # 3. 정비 창구 비어있는 곳에 대기하고 있는 사람옮기기
        for i in range(M):
            # 현재 창구가 비어있고, 기다리는 사람이 있으면
            if repair[i] == -1 and repair_wait:
                # 그 사람을 정비 창구로 옮기기
                visitor_idx = repair_wait.pop(0)
                repair[i] = [visitor_idx, repair_time[i] - 1]
                # 몇번 정비 창구 방문했는지 기록하기
                visitor_info[visitor_idx][1] = i
            # 비어있지 않으면
            elif repair[i] != -1:
                repair[i][1] -= 1

        # 4. 접수 창구 비어있는 곳에 대기열 사람 옮기기
        for i in range(N):
            # 접수창구가 비어있고, 대기 중인 사람이 있으면
            if reception[i] == -1 and reception_wait:
                visitor_idx = reception_wait.pop(0)
                # 방문한 고객 번호, 방문 시간
                reception[i] = [visitor_idx, reception_time[i] - 1]
                # 몇번 접수 창구 방문했는지 기록하기
                visitor_info[visitor_idx][0] = i
            # 비어있지 않으면
            elif reception[i] != -1:
                reception[i][1] -= 1

        # 5. 모든 창구 사람 남은 시간 -1 해주기, 위 3, 4에서 함께 처리 해줌
        time += 1
        if time > K:
            for i in range(K):
                if visitor_info[i][1] == -1:
                    break
            else:
                flag = False

    answer = 0
    for i in range(K):
        # 인덱스를 그대로 줬으니까 -1 하기
        if visitor_info[i][0] == A - 1 and visitor_info[i][1] == B - 1:
            # but 고객번호는 1부터니까 +1
            answer += i + 1

    # 고객이 없는 경우
    if answer == 0:
        answer = -1

    print(f'#{tc} {answer}')