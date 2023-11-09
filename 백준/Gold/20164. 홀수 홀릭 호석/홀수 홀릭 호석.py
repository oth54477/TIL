import sys
from itertools import combinations

input = sys.stdin.readline

N = input().strip()

def sum_string(*numbers):
    return str(sum(map(int, numbers)))

def odd_checker(n):
    count = 0
    for s in n:
        if int(s) % 2 != 0:
            count += 1
    return count

def cut_3(n, count):
    for case in combinations(range(1, len(n)), 2):
        x, y ,z = n[:case[0]], n[case[0]: case[1]], n[case[1]:]
        new_number = sum_string(x, y, z)
        now_count = count + odd_checker(new_number)
        count_odd(new_number, now_count)

def cut_2(n, count):
    mid = len(n)//2
    x, y = n[:mid], n[mid:]
    new_number = sum_string(x, y)
    now_count = count + odd_checker(new_number)
    count_odd(new_number, now_count)

def count_odd(n, count):
    l = len(n)
    if l == 1:
        max_odd_count[0] = max(max_odd_count[0], count)
        min_odd_count[0] = min(min_odd_count[0], count)
        return
    if l> 2:
        cut_3(n, count)
    elif l == 2:
        cut_2(n, count)

max_odd_count = [0]
min_odd_count = [9999999999999999]

count_odd(N, odd_checker(N))

print(min_odd_count[0], max_odd_count[0])