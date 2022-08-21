arr = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
max_idx = f'{1} {1}'

for row in range(9):
    for col in range(9):
        num = arr[row][col]
        if max_num < num:
            max_num = num
            max_idx = f'{row+1} {col+1}'
print(f'{max_num}\n{max_idx}')