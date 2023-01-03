def solution(data, col, row_begin, row_end):
    temp = 0
    result = 0
    sorted_data =  sorted(data, key=lambda x: (x[col - 1], -x[0]))
    for i in range(row_begin, row_end + 1):
        for j in sorted_data[i - 1]:
            temp += j % i
        result ^= temp
        temp = 0
    return result