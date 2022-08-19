n = int(input())

arr = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    result = []
    q = [n, i]
    while True:
        q.insert(2, q[0] - q[1])
        # print(result)
        if q[2] < 0:
            result += q[:2]
            break
        result.append(q.pop(0))
    arr[i] = result
ml = max(list(map(lambda x: len(x), arr)))
print(ml)
print(*arr[list(map(lambda x: len(x), arr)).index(ml)])
