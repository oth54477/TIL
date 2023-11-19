import sys
from itertools import combinations

input = sys.stdin.readline

H, W = map(int, input().strip().split())

def check(r, c):
    right, left = False, False
    left_c = c - 1
    while left_c >= 0:
        if blocks[r][left_c] == 1:
            left = True
            break
        left_c -= 1
    right_c = c + 1
    while right_c < W:
        if blocks[r][right_c] == 1:
            right = True
            break
        right_c += 1
    return (right and left), left_c, right_c

blocks = [[0] * W for _ in range(H)]

for c, v in enumerate(list(map(int, input().strip().split()))):
    for r in range(H-1, H-1-v, -1):
        blocks[r][c] = 1

count = 0
for c in range(1, W-1):
    for r in range(H-1, -1, -1):
        if blocks[r][c] == 0:
            result, l_c, r_c = check(r, c)
            if result:
                for i in range(l_c + 1, r_c):
                    blocks[r][i] = 1
                    count += 1
print(count)
