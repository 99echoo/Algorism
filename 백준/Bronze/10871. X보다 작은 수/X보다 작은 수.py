a = list(map(int,input().split()))
b = list(map(int,input().split()))

list = []

for i in range(a[0]):
    if b[i] < a[1]:
        list.append(b[i])
    else :
        pass

for value in list:
    print(value)