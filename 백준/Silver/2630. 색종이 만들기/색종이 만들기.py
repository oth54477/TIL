import sys

input = sys.stdin.readline


def chk(arr, depth):
  global b_count, w_count
  n = N//(2 ** depth)
  if n == 1:
    if arr[0][0] == 1:
      b_count += 1
    else:
      w_count += 1
    return
  if arr[0][0] == 1:
    flag = True
  else:
    flag = False
  for i in range(n):
    temp = sum(arr[i])
    if (temp == 0 and flag == False) or temp == n and flag == True:
      pass
    else:
      k = n // 2
      for i in [0, k]:
          chk([row[0:k] for row in arr[0+i:i+k]], depth+1)
          chk([row[k:n] for row in arr[0+i:i+k]], depth+1)
      return 
  if flag:
    b_count += 1
  else:
    w_count += 1
  
  return

N = int(input().strip())

paper = [list(map(int, input().strip().split())) for _ in range(N)]
b_count, w_count = 0, 0
chk(paper, 0)
print(w_count, b_count, sep='\n')