import sys
input = sys.stdin.readline

S = input().strip()

k_count = 0
k_arr = []
r_count = 0
r_arr = []
for idx, s in enumerate(S):
    if s == "R":
        r_count += 1
        r_arr.append(idx)
    else:
        k_count += 1
    k_arr.append(k_count)

i, j = 0, r_count - 1
left, right = 0, idx
result = 0
now_r = r_count
while left <= right:
    if j >= 0 and i <= r_count-1:
        left, right = r_arr[i], r_arr[j]
    else:
        break
    l, r = k_arr[left], k_count - k_arr[right]
    result = max(result, (now_r + 2*min(r, l)))
    if left == right:
        break
    if r > l:
        if i < r_count-1:
            i += 1
            now_r -= 1
            left = r_arr[i]
        else:
            break
    elif r < l:
        if j > 0:
            j -= 1
            now_r -= 1
            right = r_arr[j]
        else:
            break
    else:
        if j > 0 and i < r_count-1:
            i += 1
            j -= 1
            now_r -= 2
            left, right = r_arr[i], r_arr[j]
        else:
            break

print(result)