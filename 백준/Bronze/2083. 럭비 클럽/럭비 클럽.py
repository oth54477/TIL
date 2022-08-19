arr = []
while True:
    h = input().split()
    if h[0] == '#':
        break
    arr.append(h)

for value in arr:
    if int(value[1]) > 17 or int(value[2]) >= 80:
        print(value[0], 'Senior')
    else:
        print(value[0], 'Junior')
