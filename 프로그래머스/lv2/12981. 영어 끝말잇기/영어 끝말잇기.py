def solution(n, words):
    old_word = ""
    visited = set()
    for idx, now_word in enumerate(words):
        if not old_word:
            old_word = now_word
            visited.add(now_word)
        else:
            if old_word[-1] != now_word[0] or now_word in visited:
                x, y = divmod(idx, n)
                return [y+1, x+1]
            else:
                old_word = now_word
                visited.add(now_word)

    return [0, 0]