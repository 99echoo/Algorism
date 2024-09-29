a = int(input())

## list를 반복해서 입력받는 코드 작성
num_list = []


def push(x):
    num_list.append(x)
    return num_list

def pop():
    if num_list:
        print(num_list[-1])
        del num_list[-1]
    else:
        print(-1)
    return num_list

def size():
    x = len(num_list)
    return print(x)

def empty():
    if not num_list:
        print(1)
    else:
        print(0)

def top():
    if num_list:
       print(num_list[-1])
    else: 
        print(-1)


for i in range(a):
    aa = input()
    if  'push' in aa:
         _, b = aa.split()
         push(b)
    elif aa == 'pop' :
         pop()
    elif aa == 'size' :
         size()
    elif aa == 'empty' :
         empty()
    else:
         top()