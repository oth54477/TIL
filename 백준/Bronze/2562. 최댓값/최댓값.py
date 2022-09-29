arr = [int(input()) for _ in range(9)]
max_n = max(arr)
max_idx = arr.index(max_n)
print(max_n)
print(max_idx+1)