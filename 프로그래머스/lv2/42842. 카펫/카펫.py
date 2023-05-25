def solution(brown, yellow):
    a = 1
    b = -(2+brown//2)
    c = brown + yellow

    temp = int((b ** 2 - (4 * a * c)) ** (0.5))
    y1 = (-b+temp) // (2)
    y2 = (-b-temp) // (2)
    return [max(y1, y2), min(y1, y2)]