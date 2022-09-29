def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]

n = int(input())
m = int(input())
parent = list(range(n))
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            x_root, y_root = find_set(i), find_set(j)  # Find
            # Union
            if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
                if x_root < y_root:
                    parent[y_root] = x_root
                else:
                    parent[x_root] = y_root
plan = set(map(lambda x: parent[int(x) - 1], input().split()))
if len(plan) == 1:
    print('YES')
else:
    print('NO')