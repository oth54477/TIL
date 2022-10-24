from itertools import permutations
def solution(numbers):
    result = set()
    for x, y in permutations(numbers, 2):
        result.add(x + y)
    return sorted(result)