n = int(input())

list_2 = []

for i in range(n):
    order = list(map(str,input().split()))
    
    reverse = [word[::-1] for word in order]
    for value in reverse:
      print(value)