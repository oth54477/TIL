def solution(s, n):
    result = ""
    arr = list(map(lambda x : ord(x), s))
    for i in arr:
        if i == 32:
            result += " "
        else:
            if (97 <= i <= 122 and 97 <= i + n <= 122) or (65 <= i <= 90 and 65 <= i + n <= 90):
                result += chr(i + n)
            else:
                result += chr(i + n - 26)
                
    return result

    
