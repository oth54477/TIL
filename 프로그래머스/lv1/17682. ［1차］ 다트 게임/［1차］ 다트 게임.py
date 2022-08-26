def solution(dartResult):
    queue = list(map(str, dartResult))
    
    result_stack = []
    while queue:
        value = queue.pop(0)

        if value.isdigit():
            value = int(value)
            squared = queue.pop(0)
            if squared.isdigit():
                value = 10
                squared = queue.pop(0)
            if squared == 'D':
                value = value**2
            elif squared == 'T':
                value = value**3
            result_stack.append(value)
        elif value == '*':
            pop2 = result_stack.pop()
            if result_stack:
                pop1 = result_stack.pop()
                result_stack.append(pop1 * 2)
            result_stack.append(pop2 * 2)

        elif value == '#':
            pop1 = result_stack.pop()
            result_stack.append(pop1 * -1)

    answer = sum(result_stack)

    return answer