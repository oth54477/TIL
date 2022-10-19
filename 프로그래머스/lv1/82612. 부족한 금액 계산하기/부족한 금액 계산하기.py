def solution(price, money, count):
    pay = money - price * sum(range(1, count+1))
    return -pay if pay < 0 else 0