N = int(input())
words = []
cnt = 0
for i in range(N):
    word = input()
    word_list = list(word)
    result = True
    for s in word:
        if word_list.count(s) > 1:
            s_list = []
            while result:
                try:
                    num = word_list.index(s)
                    word_list.remove(s)
                    word_list.insert(num, 0)
                    s_list.append(num)
                except:
                    break
            for k in range(len(s_list) - 1):
                if s_list[k] + 1 != s_list[k + 1]:
                    result = False
                    break
    if result == True:
        cnt += 1
print(cnt)
