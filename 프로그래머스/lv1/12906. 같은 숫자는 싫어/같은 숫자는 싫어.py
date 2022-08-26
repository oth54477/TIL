def solution(arr):
    result = []
    for idx in range(len(arr) - 1):
        if arr[idx] != arr[idx + 1]:
            result.append(arr[idx])
    result.append(arr[-1])
    return result