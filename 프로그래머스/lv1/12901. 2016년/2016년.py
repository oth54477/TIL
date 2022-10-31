def solution(a, b):
    month_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    sum_date = 0
    for i in range(1, a):
        sum_date += month_dict[i]
    sum_date += b
    day_dict = {0: 'THU', 1: 'FRI',2: 'SAT',3: 'SUN',4: 'MON',5: 'TUE',6: 'WED'}
    return day_dict[sum_date % 7]