def solution(s):
    zero, count = 0, 0
    while s != "1":
        c = s.count("0")
        zero += c
        l = format(len(s.replace("0", "")), 'b')
        s = l
        count += 1
    return [count, zero]