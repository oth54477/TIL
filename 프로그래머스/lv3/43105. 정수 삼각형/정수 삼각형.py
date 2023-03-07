def solution(triangle):
    prev_row = triangle[0]
    for row in triangle[1:]:
        curr_row = []
        for i, v in enumerate(row):
            if i == 0:
                curr_row.append(v + prev_row[0])
            elif i == len(row)-1:
                curr_row.append(v + prev_row[-1])
            else:
                curr_row.append(v + max(prev_row[i-1:i+1]))
        prev_row = curr_row
    return max(prev_row)