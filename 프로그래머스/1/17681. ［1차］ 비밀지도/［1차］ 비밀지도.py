def solution(n, arr1, arr2):
    return ["".join(map(lambda x: "#" if x=="1" else " " ,format(arr1[i] | arr2[i], 'b').zfill(n))) for i in range(n)]