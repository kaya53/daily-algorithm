import sys

sys.stdin = open('input.txt')


def arrive(cus_no):
    for r_no in recept_desk:
        if not recept_desk[r_no]:
            recept_desk[r_no] = [cus_no, recept_time[r_no]]
            break
    else:
        wait_recept.append(cus_no)


def to_repair(cus_no):
    for p_no in repair_desk:
        if not repair_desk[p_no]:
            repair_desk[p_no] = [cus_no, repair_time[p_no]]
            break
    else:
        wait_repair.append(cus_no)


T = int(input())
for tc in range(1):
    N, M, K, A, B = map(int, input().split())
    recept_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    visit_time = list(map(int, input().split()))

    time = -1
    recept_desk = dict.fromkeys(range(N), [])
    repair_desk = dict.fromkeys(range(M), [])
    wait_recept = []
    wait_repair = []
    while True:
        # 접수 창구와 정비 창구의 소요 시간 1씩 빼주기
        # 종료조건: 마지막 고객이 정비 창구에 들어갔을 때
        time += 1
        for r_no, r_val in recept_desk.items():
            if not r_val: continue
            recept_desk[r_no][1] -= 1
        for p_no, p_val in repair_desk.items():
            if not p_val: continue
            repair_desk[p_no][1] -= 1

        # 고객 도착
        if wait_recept:
            wait_recept.sort(reverse=True)
            arrive(wait_recept.pop())
        for cus in range(K):
            if visit_time[cus] == time:
                # 기다리고 있는 사람 있으면 그 사람 보내기
                arrive(cus)

        # 정비 창구 => 접수 창구: 두번째 요소가 0인 애들
        if wait_repair:
            wait_repair.sort(reverse=True)
            to_repair(wait_repair.pop())

        for r_no, r_val in recept_desk.items():
            if not r_val: continue
            if not r_val[1]:
                to_repair(r_val[0])
                recept_desk[r_no] = []



