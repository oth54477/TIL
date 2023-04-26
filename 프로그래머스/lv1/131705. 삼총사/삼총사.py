def solution(number):
    from itertools import combinations
    count = 0
    for case in combinations(number, 3):
        if sum(case) == 0:
            count += 1
    return count