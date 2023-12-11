import sys

input = sys.stdin.readline

N, S = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

left, right = 0, 0

result = 999999999999
sum_value = arr[0]

def count():
    return right - left + 1

while left < N:
    if sum_value >= S:
        result = min(result, count())
        if result == 1:
            break
        if left < right:
            sum_value -= arr[left]
            left += 1
        elif right < N-1:
                right += 1
                sum_value += arr[right]
    elif right < N-1:
            right += 1
            sum_value += arr[right]
    else:
        break
if result == 999999999999:
    result = 0

print(result)