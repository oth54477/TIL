import sys

input = sys.stdin.readline

word_list = list(map(str, (input().strip())))
word_length = len(word_list)

result = [""] * word_length

def solution(start, word):
    if not word:
        return
    min_s = min(word)
    idx = word.index(min_s)

    result[start + idx] = min_s
    print("".join(result))
    solution(start+idx+1, word[idx+1:])

    solution(start, word[:idx])
    
solution(0,word_list)