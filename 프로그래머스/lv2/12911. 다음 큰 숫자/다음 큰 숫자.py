def solution(n):
    s = format(n, "b").count("1")
    while True:
        n += 1
        if format(n, "b").count("1") == s:
            return n