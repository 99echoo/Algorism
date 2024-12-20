A = list(map(str,input()))

stack = []
total_species = 0

for i in range(len(A)):
  if A[i] == '(': # 여는 괄호의 경우
     stack.append(A[i])
  else : # 닫는 괄호의 경우
     if A[i-1] == '(' : # 레이저 !
        stack.pop()
        total_species += len(stack)
     else :
        stack.pop()
        total_species += 1

print(total_species)

       