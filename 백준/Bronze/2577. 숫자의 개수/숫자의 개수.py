n = int(input())
m = int(input())
k = int(input())
a = n * m * k
a = str(a)
for i in range(10):
    print(a.count(str(i)))