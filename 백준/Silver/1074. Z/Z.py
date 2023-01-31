import sys

input = sys.stdin.readline

N, r, c = map(int, input().strip().split())
cnt = 0

while N > 1:
    size = (2**N) // 2
    if r < size and c < size:
        pass
    elif r < size and c >= size:
        cnt += size ** 2
        c -= size
    elif r >= size and c < size:
        cnt += size ** 2 * 2
        r -= size
    elif r >= size and c >= size:
        cnt += size ** 2 * 3
        r -= size
        c -= size
    N -= 1

if r == 0 and c == 0:
    pass
elif r == 0 and c == 1:
    cnt += 1
elif r == 1 and c == 0:
    cnt += 2
elif r == 1 and c == 1:
    cnt += 3
print(cnt)