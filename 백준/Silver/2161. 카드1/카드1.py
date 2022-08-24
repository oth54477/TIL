n = int(input())

queue = []
result = []
for v in range(1, n + 1):
    queue.append(v)
while True:
    result.append(queue.pop(0))
    if len(result) == n:
        break
    queue.append(queue.pop(0))

print(*result)
