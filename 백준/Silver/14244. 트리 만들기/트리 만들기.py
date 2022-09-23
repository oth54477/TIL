n,m = map(int, input().split())

nums = list(range(n))

num = nums[:-(m-1)]
nn = nums[-(m-1):]
for i in range(len(num)-1):
    print(num[i], num[i+1])
for j in nn:
    print(num[-1], j)
