def solution(x):
    return False if x % sum([int(n) for n in str(x)]) != 0 else True