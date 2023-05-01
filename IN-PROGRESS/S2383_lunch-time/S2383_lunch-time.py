import sys

sys.stdin = open('sample_input.txt')


def check(choice):
    global mmin
    
    # 초기 시간 설정
    time_ls = [0] * P
    for p in range(P):
        ci, cj = ppl[p]
        sti, stj = stairs[choice[p]-1][:2]
        time_ls[p] = abs(ci-sti) + abs(cj-stj)
    
    # 계단에 올라온 사람 표시
    stair_q = [[], []]
    t = 0
    in_stair = [0] * P
    
    # 모든 사람이 이동 완료할 때까지
    while sum(time_ls) != 0 or stair_q[0] or stair_q[1]:
        t += 1
        
        # 가지치기
        if t >= mmin: return 
        
        # 계단에 올라온 사람들 시간 하나씩 빼주고, 0이면 큐에서 빼기
        for q in stair_q:
            while q:
                for _ in range(len(q)):
                    now = q.pop(0)
                    now -= 1
                    if now: q.append(now)
                break

        for ppl_no in range(P):
            if time_ls[ppl_no]: time_ls[ppl_no] -= 1
            now_stair = choice[ppl_no] - 1
            # q = stair_q[now_stair]
            
            # 계단까지 이동함 + 계단에 빈 자리 있음 + 계단을 아직 타지 않은 사람
            if not time_ls[ppl_no] and len(stair_q[now_stair]) < 3 and not in_stair[ppl_no]:
                stair_q[now_stair].append(stairs[now_stair][-1])  # 계단 도착 표시
                in_stair[ppl_no] = 1

    mmin = min(mmin, t+1)


def comb(idx):
    if idx == P:
        check(choice)
        return

    for i in [1, 2]:
        choice[idx] = i
        comb(idx+1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ppl = []
    stairs = []
    for n in range(N):
        for m in range(N):
            if arr[n][m] == 1:
                ppl.append((n, m))
            elif arr[n][m] > 1:
                stairs.append([n, m, arr[n][m]])
    P = len(ppl)

    choice = [0] * P
    mmin = int(1e9)
    comb(0)
    print(f'#{tc} {mmin}')