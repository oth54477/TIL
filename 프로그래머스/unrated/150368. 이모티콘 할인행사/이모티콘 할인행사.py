def solution(users, emoticons):
    def dfs(arr, depth, L):
        for i in [10,20,30,40]:
            arr.append(i)
            if depth == L:
                plus, total_pay = chk(arr)
                if plus > case[0]:
                    case[0], case[1] = plus, total_pay
                elif plus == case[0] and total_pay > case[1]:
                    case[0], case[1] = plus, total_pay
            else:
                dfs(arr, depth+1, L)
            arr.pop()

    def chk(arr):
        plus = 0
        total_pay = 0
        for user in users:
            pay = 0
            for idx in range(L):
                if user[0] <= arr[idx]:
                    pay += ((100 - arr[idx]) / 100) * emoticons[idx]
                    if pay >= user[1]:
                        plus += 1
                        break
            else:
                total_pay += pay
        return plus, int(total_pay)
    max_plus = [0]
    case = [0, 0]
    L = len(emoticons)
    dfs([], 1, L)
    return case