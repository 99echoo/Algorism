A = input()

Answer = len(A)
i = 0

while i < len(A):
    if i < len(A) - 2 and A[i:i+3] == 'dz=':
        Answer -= 2
        i += 3
    elif i < len(A) - 1 and A[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        Answer -= 1
        i += 2
    else:
        i += 1

print(Answer)