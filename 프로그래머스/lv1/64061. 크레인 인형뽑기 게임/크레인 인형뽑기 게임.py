def solution(board, moves):
    r_board = list(map(list, zip(*board)))
    l = len(r_board[0])
    box = []
    cnt = 0
    for i, b in enumerate(r_board):
        while 0 in b:
            r_board[i].pop(b.index(0))
    for t in moves:
        if r_board[t-1]:
            s = r_board[t-1].pop(0)
            if box and box[-1] == s:
                box.pop()
                cnt += 2
            else:
                box.append(s)

    return cnt