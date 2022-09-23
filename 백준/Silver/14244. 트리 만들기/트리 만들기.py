n,m = map(int, input().split())

nums = list(range(n))

nodes = nums[:-(m-1)]
lead = nums[-(m-1):]
for i in range(len(nodes)-1):
    print(nodes[i], nodes[i+1])
for j in lead:
    print(nodes[-1], j)
