a = int(input())
b = list(map(int, input().split()))
c = int(input())

answer = 0

for i in range(a):
  if c == b[i]:
    answer += 1
  else :
    pass

print(answer)