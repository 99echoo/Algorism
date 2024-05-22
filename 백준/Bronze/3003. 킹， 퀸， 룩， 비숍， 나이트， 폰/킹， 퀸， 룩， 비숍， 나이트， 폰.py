program = list(map(int, (input().split())))

array = [1,1,2,2,2,8]

for i in range(len(program)):
   
   program[i] = array[i] - program[i]
   
print(*program)