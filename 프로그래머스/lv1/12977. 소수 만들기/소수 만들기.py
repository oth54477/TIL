from itertools import combinations
import math

def solution(numbers):
    cnt = 0
    for x, y, z in combinations(numbers, 3):
        num = x + y + z
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        else:
            cnt += 1
    return cnt