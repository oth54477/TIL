T = int(input())

for t in range(1, T + 1):
    num1, num2 = map(int, input().split())  # 입력받은 두 수를 num1과 num2에 저장

    if num1 > num2:  # num1이 num2보다 크다면 '>'
        result = '>'
    elif num1 < num2:  # num1이 num2보다 작다면 '<'
        result = '<'
    else:  # 둘다 아니라면 '='
        result = '='

    print(f'#{t} {result}')
