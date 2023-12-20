def solution(elements):
    l = len(elements)
    sum_set = set()
    for i in range(1, l+1):
        window = 0
        linked_list = elements[l-i+1:] + elements + elements[:i-1]
        for j in linked_list[:i]:
            window += j
        sum_set.add(window)
        for k in range(i, l+(2*(i-1))):
            window -= linked_list[k-i]
            window += linked_list[k]
            sum_set.add(window)

    return len(sum_set)
