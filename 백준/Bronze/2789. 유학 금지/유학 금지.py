word = input()

word_filter = 'CAMBRIDGE'

for s in word_filter:
    word = word.replace(s, '')
print(word)
