for t in range(1, int(input()) + 1):
    input()
    nums = {}
    arr = map(int, input().split())

    for num in arr:
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 0

    print(f'#{t} {sorted(nums, key=lambda x: nums[x], reverse=True)[0]}')