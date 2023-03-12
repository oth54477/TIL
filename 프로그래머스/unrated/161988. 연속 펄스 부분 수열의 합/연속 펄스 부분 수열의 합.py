def solution(sequence):
    dp = [0]
    for idx, value in enumerate(sequence):
        if is_even(idx):
            dp.append(dp[-1] + value)
        else:
            dp.append(dp[-1] - value)
    return max(dp) - min(dp)
    

def is_even(number):
        if number % 2 == 0:
            return True
        return False

print(solution([2, 3, -6, 1, 3, -1, 2, 4]))