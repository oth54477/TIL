def solution(n, m, x, y, r, c, k):
    dist = abs(x - r) + abs(y - c)
    margin = k - dist
    if margin < 0 or margin%2 != 0:
        return "impossible"

    result = ''
    direction = {"d": 0, "l": 0, "r": 0, "u": 0}
    if x > r:
        direction["u"] += x-r
    else:
        direction["d"] += r-x
    if y > c:
        direction["l"] += y-c
    else:
        direction["r"] += c-y

    result += "d"*direction["d"]
    d = min(int(margin/2), n-(x+direction["d"]))
    result += "d"*d
    direction["u"] += d
    margin -= 2*d

    result += "l"*direction["l"]
    l = min(int(margin/2), y-direction["l"]-1)
    result += "l"*l
    direction["r"] += l
    margin -= 2*l

    result += "rl"*int(margin/2)
    result += "r"*direction["r"]
    result += "u"*direction["u"]

    return result