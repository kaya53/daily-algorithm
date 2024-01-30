def get_degree(h, m, s):
    res = -1
    hd = ((h * 30) + (m * 0.5) + (s * (0.5 / 60))) % 360
    md = ((m * 6) + (s * 0.1)) % 360
    sd = (s * 6)
    # 끝나는 초가 더 앞서 있으면 => 분침을 스쳐간 것
    if sd >= md: res += 1
    if sd >= hd: res += 1

    res += ((h * 60) + m) * 2  # 분당 2회 만남
    res -= h  # 매 시 59분 00초 ~ 0분 00초 1번만 만남
    if h >= 12: res -= 2  # 11:59:00 ~ 12:00:00
    return res


def solution(h1, m1, s1, h2, m2, s2):
    answer = get_degree(h2, m2, s2) - get_degree(h1, m1, s1)
    if ((h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0):
        answer += 1

    return answer