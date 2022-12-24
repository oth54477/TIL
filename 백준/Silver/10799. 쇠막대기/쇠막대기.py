import sys
input = sys.stdin.readline

pole = input()
pole_cnt, cnt, idx = 0, 0, 0
while idx < len(pole):
    if idx != len(pole) - 1 and pole[idx] + pole[idx + 1] == '()':
        pole_cnt += cnt
        idx += 1
    elif pole[idx] == ')':
        cnt -= 1
        pole_cnt += 1
    else:
        cnt += 1
    idx += 1
print(pole_cnt)