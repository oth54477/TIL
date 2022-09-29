for t in range(int(input())):
    a = input()
    cnt, score = 0, 0
    for i in a:
        if i == 'X':
            cnt = 0
        else:
            cnt+=1
            score += cnt
    print(score)
            