rn =  int(input())
input_  = list(map(int,input().split()))

input_.sort()

answer = input_[0] * input_[-1]

print(answer)