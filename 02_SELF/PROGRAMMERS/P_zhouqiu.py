import math


def solution(m, n, sx, sy, balls):
    answer = []
    INF = int(1e9)
    dots = [(0, 0), (0, m), (0, n), (m, n)]

    for tx, ty in balls:
        mmin = INF
        # 3번째 flipped에 m+m+tx라 잘못 써서 에러났음
        flipped = [(tx, n + n - ty), (tx, -1 * ty), (-1 * tx, ty), (m + (m - tx), ty)]
        for idx, now in enumerate(flipped):  # 위, 아래, 왼, 오
            nx, ny = now
            # 일직선으로 가다가 공에 맞는 경우
            if idx == 0 and sx == tx and sy < ty: continue
            if idx == 1 and sx == tx and sy > ty: continue
            if idx == 2 and sy == ty and sx > tx: continue
            if idx == 3 and sy == ty and sx < tx: continue
            dist = (nx - sx) ** 2 + (ny - sy) ** 2
            mmin = min(mmin, dist)

        for idx, dot in enumerate(dots):  # 꼭지점
            dx, dy = dot
            if ty == tx * ((sy - dy) / (sx - dx)):
                dist = -1
                if (idx < 2 and sx < tx) or (idx >= 2 and sx > tx):
                    dist = math.sqrt((tx - dx) ** 2 + (ty - dy) ** 2) + math.sqrt((sx - dx) ** 2 + (sy - dy) ** 2)
                    # print('꼭지점: ', (tx, ty), (dx, dy), dist**2)
                if dist > -1:
                    mmin = min(mmin, round(dist ** 2))

        answer.append(mmin)

    return answer