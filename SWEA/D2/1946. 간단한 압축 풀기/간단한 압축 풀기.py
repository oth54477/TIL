T=input()
for i in range(0,int(T)):
    N = input()
    t=''
    for j in range(0,int(N)):
        x=str(input()).split()
        t += x[0]*int(x[1])
        L = len(t)
    print('#'+str(i+1))
    for k in range(1,L//10+2):
        print(t[slice(k*10-10,k*10)])