x, y = map(int, input().split())
n = int(input())

x_axis = [0]
y_axis = [0]

for _ in range(n):
    d, v = map(int, input().split())
    if d:
        x_axis.append(v)
    else:
        y_axis.append(v)

x_axis.append(x)
y_axis.append(y)

x_axis.sort()
y_axis.sort()

x_value, y_value = [], []
for idx, x in enumerate(x_axis[:-1]):
    x_value.append(x_axis[idx + 1] - x)
for idx, y in enumerate(y_axis[:-1]):
    y_value.append(y_axis[idx + 1] - y)

result = []
for x in x_value:
    for y in y_value:
        result.append(x * y)

print(max(result))
