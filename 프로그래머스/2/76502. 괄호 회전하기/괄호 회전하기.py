def solution(s):
    ll = len(s)
    cnt = 0
    table = {"]": "[", "}": "{", ")": "("}
    s = s + s
    for i in range(ll):
        ss = s[i:i+ll]
        stack = []
        for j in range(ll):
            if ss[j] in {"[", "{", "("}:
                stack.append(ss[j])
            else:
                if stack and stack[-1] == table[ss[j]]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                cnt += 1
    return cnt
    