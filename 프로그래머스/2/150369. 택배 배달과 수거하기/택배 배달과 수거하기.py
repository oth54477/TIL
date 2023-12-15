def solution(cap, n, deliveries, pickups):
    result = 0
    last_house = n
    last_d_house, last_p_house = n, n
    while True:
        if last_house == 0:
            break
        temp_cap = cap
        cap_space = cap - temp_cap
        for k in range(last_house-1, -1, -1):
            d, p = deliveries[k], pickups[k]
            if d == 0 and p == 0:
                last_house = k
            else:
                break
        result += (last_house * 2)
        for i in range(last_d_house-1, -1, -1):
            d = deliveries[i]
            # 전부 배달이 가능한 경우
            if temp_cap >= d:
                temp_cap -= d
                deliveries[i] = 0
                last_d_house = i
            # 전부 배달이 불가능한 경우
            else:
                deliveries[i] = d - temp_cap
                temp_cap = 0
                break

        cap_space = cap
        for j in range(last_p_house-1, -1, -1):
            p = pickups[j]
            # 전부 수거가 가능한 경우
            if cap_space >= p:
                cap_space -= p
                pickups[j] = 0
                last_p_house = j
            # 전부 수거가 불가능한 경우
            else:
                pickups[j] = p - cap_space
                cap_space = 0
                break

        last_house = max(last_d_house, last_p_house)
    return result