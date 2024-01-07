import sys
from itertools import product

input = sys.stdin.readline

N,K = map(int,input().split())
arr = list(map(str,input().split()))
length = len(str(N))

while(True):
    temp = list(product( arr, repeat=length))
    result = []

    for i in temp :
        if int("".join(i)) <= N :
            result.append(int("".join(i)))

    if len(result)>= 1:
        print(max(result))
        break
    else : 
        length -=1