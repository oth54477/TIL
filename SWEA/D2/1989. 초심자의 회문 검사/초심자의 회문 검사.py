n=input()
for i in range(0,int(n)):
    text = input()
    if text == text[::-1]:
        print('#'+str(i+1), '1')
    else:
        print('#'+str(i+1), '0')