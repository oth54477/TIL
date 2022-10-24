from itertools import combinations
def solution(numbers):
    return sorted({(x + y) for x, y in combinations(numbers, 2)})