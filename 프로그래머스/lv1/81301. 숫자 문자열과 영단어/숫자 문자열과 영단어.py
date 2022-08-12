def solution(s):
    table = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for idx, word in enumerate(table):
        if word in s:
            s = s.replace(word, str(idx))
    return int(s)