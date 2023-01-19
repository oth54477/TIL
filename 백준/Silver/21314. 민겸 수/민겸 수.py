import sys

input = sys.stdin.readline

string = input().strip().replace('K', ' K ').split()

result = ''
temp = ''
min_temp = ''
for s in string:
    if 'M' in s:
        # result += temp
        l = s.count('M')
        # temp += '1'+'0'*(l-1)
        temp += '1'*len(s)
        min_temp += str(10**(len(s)-1))
    else:
        if temp != '':
            result += str((10**len(temp))*5)
            temp = ''
        else:
            result += temp
            result += '5'
        min_temp += '5'
print(result+temp)
print(min_temp)