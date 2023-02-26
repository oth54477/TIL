def solution(numbers):
    result = numbers[:]
    stack = []
    for idx, number in enumerate(numbers):
        while stack:
            if stack[-1][1] < number:
                small_idx, small_number = stack.pop()
                result[small_idx] = number
            else:
                break
        stack.append((idx, number))
    while stack:
        idx, number = stack.pop()
        result[idx] = -1
    return result