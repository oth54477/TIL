def solution(plans):
    plans = sorted(plans, key=lambda x: x[1], reverse=True)
    result = []
    waiting = []
    old = plans.pop()
    old1 = chk_time(old[1])
    old2 = int(old[2])
    while plans:
        # 과제는 시작하기로 한 시각이 되면 시작합니다.
        now = plans.pop()
        now1 = chk_time(now[1])
        now2 = int(now[2])

        temp = old1 + old2 - now1

        # 새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다.
        if temp > 0:
            waiting.append([old[0], temp])
        # 진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다.
        elif temp < 0:
            result.append(old[0])
            while waiting and temp < 0:
                temp += waiting[-1][1]
                if temp <= 0:
                    result.append(waiting.pop()[0])
                else:
                    waiting[-1][1] = temp
        # 만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
        else:
            result.append(old[0])
        old = now
        old1 = now1
        old2 = now2
    result.append(now[0])
    # 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다.
    while waiting:
        result.append(waiting.pop()[0])

    return result

def chk_time(s):
    s1, s2 = map(int, s.split(":"))
    return s1 * 60 + s2