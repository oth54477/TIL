def solution(sizes):
    min_of_max = 0
    max_size = 0
    for size in sizes:
        now_max_size = max(size)
        now_min_size = min(size)
        max_size = max(max_size, now_max_size)
        min_of_max = max(min_of_max, now_min_size)
    return max_size * min_of_max
    