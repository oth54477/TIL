words = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0
for alph in croatia:
    if alph in words:
        cnt += words.count(alph)
        words = words.replace(alph, '0')


words = words.replace('0', '')
cnt += len(words)

print(cnt)
