for t in range(1,int(input())+1):
    text = input()
    if text == text[::-1]:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')