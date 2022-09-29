a = set()
for i in [int(input()) for _ in range(10)]:
    a.add(i % 42)
print(len(a))