import sys

data = list(map(int, [sys.stdin.readline().strip() for i in range(28)]))

data.sort()

for student in range(1, 31):
    if student not in data:
        print(student)
