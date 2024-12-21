A = list(map(int,input().split()))

stack = []
answer = []
idx = 0

for i in range(A[0]):
    stack.append(i+1)


while stack:            
      idx = (idx + A[1]-1) % len(stack)
      answer.append(stack.pop(idx)) 

print("<" + ", ".join(map(str, answer)) + ">")  # int -> str 변환 후 join