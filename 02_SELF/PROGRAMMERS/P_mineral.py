# 재귀로 풀어야 하는 이유
# 1. 3<= len(minerals)<= 50으로 크기가 작음
# 2. depth로 들어가야 하는 곡괭이도 총 개수가 15개로 많이 않아서 재귀를 타 볼만 함
# 다이아 > 철 > 돌 곡괭이 순으로 쓰면 안되는 이유
# picks = [철, 돌],  minerals=[돌 돌 돌 돌 돌 다이아 다이아 다이아 다이아 다이아]인 경우
# 돌을 먼저 쓰고 철 곡괭이를 쓰는 게 이득이다.
# 이렇게 어떤 곡괭이를 쓰는 게 이득인 지 따져볼 때 다른 광물들까지 고려를 해야 하므로 단순히 그리디로 풀기에는 무리가 있다

def recur(energy, minerals, pick_idx, m_idx, picks, m_cnt, used, ls):
    global answer

    if (sum(picks) == 0 and m_cnt == 0) or m_idx == len(minerals):
        if answer > used:
            answer = used
        return

    if m_cnt and pick_idx >= 0:
        recur(energy, minerals, pick_idx, m_idx + 1, picks, m_cnt - 1, used + energy[pick_idx][minerals[m_idx]],
              ls + [energy[pick_idx][minerals[m_idx]]])
    else:
        for i in range(3):
            if not picks[i]: continue
            picks[i] -= 1
            recur(energy, minerals, i, m_idx + 1, picks, 4, used + energy[i][minerals[m_idx]],
                  ls + [energy[i][minerals[m_idx]]])
            picks[i] += 1


answer = int(1e9)
def solution(picks, minerals):
    n = len(minerals)
    energy = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    for k in range(n):
        if minerals[k] == 'diamond':
            minerals[k] = 0
        elif minerals[k] == 'iron':
            minerals[k] = 1
        else:
            minerals[k] = 2

    recur(energy, minerals, -1, 0, picks, 0, 0, [])
    return answer