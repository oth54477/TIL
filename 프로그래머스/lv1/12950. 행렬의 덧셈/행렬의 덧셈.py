def solution(arr1, arr2):
    answer = []
    for idx in range(len(arr1)):
        answer.append([x + y for x, y in zip(arr1[idx], arr2[idx])])
    return answer