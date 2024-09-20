a = list(map(int,input().split()))

baguni = [0] * a[0]

for i in range(a[1]):
    answer = list(map(int,input().split()))
    for ball in range(answer[0]-1,answer[1]):
     baguni[ball] = answer[2]

for value in baguni:
   print(value) 