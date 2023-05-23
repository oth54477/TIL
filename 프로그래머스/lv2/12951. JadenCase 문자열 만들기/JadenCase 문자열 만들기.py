def solution(s):
    result = ""
    flag = True
    for i in s:
        if i == " ":
            result += i
            flag = True
        elif flag:
            result += i.upper()
            flag = False
        else:
            result += i.lower()
    return result