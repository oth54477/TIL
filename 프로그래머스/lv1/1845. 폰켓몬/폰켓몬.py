def solution(nums):
    set_nums = set(nums)
    num = len(set_nums)
    n_2 = len(nums) // 2
    if num > n_2:
        result = n_2
    else:
        result = num
    return result