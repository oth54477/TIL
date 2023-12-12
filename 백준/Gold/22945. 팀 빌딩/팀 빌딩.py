import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, N-1

def between_n():
    return right - left - 1

def ability(min_n):
    return between_n() * min_n

max_ability = 0

while left < right-1:
    l, r = arr[left], arr[right]
    if l < r:
        max_ability = max(max_ability, ability(l))
        left += 1
    elif l > r:
        max_ability = max(max_ability, ability(r))
        right -= 1
    else:
        max_ability = max(max_ability, ability(l))
        nl, nr = arr[left+1], arr[right-1]
        if nl >= nr:
            left += 1
        else:
            right -= 1
print(max_ability)
