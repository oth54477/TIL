def solution(numbers, hand):
    result = ''
    lx, ly = 2, 3
    rx, ry = 0, 3
    for num in numbers:
        if num == 0:
            num = 11
        x = ((num % 3) * 2) % 3
        y = num // 3 if x else num // 3 - 1
        l = abs(lx - x) + abs(ly - y)
        r = abs(rx - x) + abs(ry - y)
        if num % 3 == 1:
            lx, ly = x, y
            result += 'L'
        elif num % 3 == 0:
            rx, ry = x, y
            result += 'R'
        else:
            if l > r:
                rx, ry = x, y
                result += 'R'
            elif l < r:
                lx, ly = x, y
                result += 'L'
            else:
                if hand == 'right':
                    rx, ry = x, y
                    result += 'R'
                else:
                    lx, ly = x, y
                    result += 'L'
    return result