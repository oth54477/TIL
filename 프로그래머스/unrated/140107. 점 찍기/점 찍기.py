def solution(k, d):
    cnt = 0
    for x in range(0, d + 1, k):
        y_max = (d ** 2 - x ** 2 ) ** (0.5)
        cnt += (int(y_max) // k) + 1
    return cnt
#     cnt = 0
#     dd = d ** 2
#     ka=0
#     a=1
#     ks = [0]
#     #b= False
#     #while ka < d:
#     #    ka= k * a
#     #    ks.append(ka ** 2)
#     #    a += 1
    
#     ks = list(map(lambda x: (x * k) ** 2, list(range(0, d//k + 1))))

#     #for i in ks:
#         #if i * 2 <= dd:
#             #cnt += 1
    
#     while ks:
#         i = ks.pop(0)
#         if i + i <= dd:
#             cnt += 1
#         for j in ks:
#             if i + j <= dd:
#                 cnt += 2
#             else:
#                 #b = True
#                 break
#     return cnt