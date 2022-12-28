from collections import Counter

def solution(topping):
    count = 0
    topping_dict = Counter(topping)
    topping_set = set()
    for i in topping:
        topping_dict[i] -= 1
        topping_set.add(i)

        if topping_dict[i] == 0:
            topping_dict.pop(i)
        if len(topping_dict) == len(topping_set):
            count += 1

    return count