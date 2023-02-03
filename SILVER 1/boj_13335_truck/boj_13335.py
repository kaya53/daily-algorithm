import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

for _ in range(3):  # 나중에 빼기
    n, w, l = map(int, input().split())
    trucks = list(map(int, input().split()))

    bridge = []
    weight_sum = 0
    res_time = 1

    while trucks or bridge:
        res_time += 1  # 일단 시간 늘려주기

        # 시간이 지났으니까 큐 안에 있는 트럭에 시간 더해주기
        if bridge:
            for i in range(len(bridge)):
                bridge[i][0] += 1

        # 들어갈 수 있는 트럭은 들여보내기; 트럭이 있을 때만
        if trucks:
            if (len(bridge) < w) and weight_sum + trucks[0] <= l:
                now_t = trucks.pop(0)
                bridge.append([1, now_t])
                weight_sum += now_t
        # try:  # trucks가 비어있어도 bridge에 아직 차가 남아 있다면
        #     if (len(bridge) < w) and weight_sum + trucks[0] <= l:
        #         now_t = trucks.pop(0)
        #         bridge.append([1, now_t])
        #         weight_sum += now_t
        # except:  # 다리에 트럭이 다 들어왔는데 다리에는 아직 남아 있는 경우
        #     continue  # 바로 빠져나오기로 가야 함
        # 빠져나오기
        while bridge:
            if bridge[0][0] == w:
                out_t = bridge.pop(0)
                weight_sum -= out_t[1]
            elif bridge[0][0] < w:
                break

    print(res_time)