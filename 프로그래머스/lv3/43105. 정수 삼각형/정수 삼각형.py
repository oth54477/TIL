def solution(triangle):
    L = len(triangle)
    for row, arr in enumerate(triangle):
        if row < L-1:
            for idx, value in enumerate(triangle[row + 1]):
                prev_idx1, prev_idx2 = idx - 1, idx
                # 범위를 벗어나는 경우
                if prev_idx1 < 0:
                    prev_v1 = 0
                else:
                    prev_v1 = arr[prev_idx1]
                if row < prev_idx2:
                    prev_v2 = 0
                else:
                    prev_v2 = arr[prev_idx2]

                # 더 큰값 선택
                triangle[row+1][idx] = max(value + prev_v1, value + prev_v2)
    return max(triangle[-1])
