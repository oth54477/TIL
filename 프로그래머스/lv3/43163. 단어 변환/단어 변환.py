from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    L = len(words)
    l = len(begin)
    visited = [False] * L
    dq = deque([(begin, 0)])
    while dq:
        word, count = dq.popleft()
        for idx, next_word in enumerate(words):
            if not visited[idx]:
                cnt = 0
                for i in range(l):
                    if word[i] != next_word[i]:
                        cnt += 1
                    if cnt > 1:
                        break
                else:
                    if next_word == target:
                        return count + 1
                    dq.append((next_word, count + 1))
                    visited[idx] = True