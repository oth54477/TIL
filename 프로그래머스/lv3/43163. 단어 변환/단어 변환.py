from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    # 방문한 단어를 저장하는 리스트 대신, 집합으로 변경
    visited = set()
    dq = deque([(begin, 0)])
    
    while dq:
        word, count = dq.popleft()
        
        for next_word in words:
            if next_word not in visited and is_one_diff(word, next_word):
                if next_word == target:
                    return count + 1
                dq.append((next_word, count + 1))
                visited.add(next_word)
    
    return 0

# 두 단어가 한 개의 알파벳만 다른지 확인하는 함수
def is_one_diff(word1, word2):
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
            if diff_count > 1:
                return False
    return diff_count == 1