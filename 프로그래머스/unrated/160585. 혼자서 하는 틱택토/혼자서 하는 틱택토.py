def solution(board):
    global win_o, win_x
    temp = 1
    win_x = False
    win_o = False
    cnt_o, cnt_x = 0, 0
    for line in board:
        for value in line:
            globals()['value{}'.format(temp)] = value
            temp += 1
            if value == "O":
                cnt_o += 1
            elif value == "X":
                cnt_x += 1
    
    # 개수 확인
    if cnt_x > cnt_o:
        return 0
    if cnt_o - cnt_x > 1:
        return 0

    # 빙고 확인
    if value1 == value2 == value3 != ".":
        check(value1)
    if value4 == value5 == value6 != ".":
        check(value4)
    if value7 == value8 == value9 != ".":
        check(value7)
    if value1 == value4 == value7 != ".":
        check(value1)
    if value2 == value5 == value8 != ".":
        check(value2)
    if value3 == value6 == value9 != ".":
        check(value3)
    if value1 == value5 == value9 != ".":
        check(value1)
    if value3 == value5 == value7 != ".":
        check(value3)
    if win_o and win_x:
        return 0
    if win_o:
        if cnt_o - cnt_x != 1:
            return 0
    if win_x:
        if cnt_o != cnt_x:
            return 0
    return 1

def check(value):
    global win_o, win_x
    if value == "O":
        win_o = True
    elif value == "X":
        win_x = True