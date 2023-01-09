import sys

input = sys.stdin.readline

m = int(input())

commands_dict = {
    'add': lambda x: s.add(x),
    'remove': lambda x: s.remove(x) if x in s else None,
    'check': lambda x: print(1) if x in s else print(0),
    'toggle': lambda x: s.remove(x) if x in s else s.add(x)
    }
s = set()
for _ in range(m):
    command, *n = input().strip().split()
    if command == 'all':
        s = set(range(1, 21))
    elif command == 'empty':
        s = set()
    else:
        n = int(n[0])
        commands_dict[command](n)