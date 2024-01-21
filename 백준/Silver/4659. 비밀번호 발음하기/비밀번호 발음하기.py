import sys

input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}

good = 'is acceptable.'
bad = 'is not acceptable.'

def convert_output(pwd, flag):
    if flag:
        return f'<{pwd}> {good}'
    else:
        return f'<{pwd}> {bad}'

while True:
    pwd = input().strip()
    if pwd == 'end':
        break

    l = len(pwd)
    pwd_checker = False
    vowel_cnt = 0
    consonant_cnt = 0
    vowel_flag = False
    old_s = pwd[0]
    if old_s in vowels:
        vowel_cnt += 1
        vowel_flag = True
    else:
        consonant_cnt += 1
    for i in range(1, l):
        now_s = pwd[i]

        # 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
        if now_s in vowels:
            vowel_flag = True
            if not vowel_cnt:
                consonant_cnt = 0
            vowel_cnt += 1
        else:
            if not consonant_cnt:
                vowel_cnt = 0
            consonant_cnt += 1

        # 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        if vowel_cnt >= 3 or consonant_cnt >= 3:
            break

        # 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        if old_s == now_s:
            if not (now_s == 'e' or now_s == 'o'):
                break
        old_s = now_s
    else:
        if vowel_flag:
            pwd_checker = True
    
    if pwd_checker:
        print(convert_output(pwd, True))
    else:
        print(convert_output(pwd, False))