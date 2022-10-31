def solution(arr, divisor):
    result = []
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    result.sort()
    if not result:
        result = [-1]
    return result