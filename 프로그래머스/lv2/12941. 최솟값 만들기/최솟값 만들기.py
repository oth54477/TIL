def solution(A,B):
    temp_A = sorted(A)
    temp_B = sorted(B, reverse=True)
    return sum(map(lambda x, y: x * y, temp_A, temp_B))