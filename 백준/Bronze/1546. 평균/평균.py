a = int(input())
b = list(map(int,input().split()))

key = max(b)

for i in range(a):
    b[i] = (b[i] / key) * 100

answer =  sum(b) / len(b)
print(answer)