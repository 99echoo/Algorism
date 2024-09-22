a = list(map(int,input().split()))

result_1 = (a[0] + a[1]) % a[2]
result_2 = ((a[0] % a[2]) + (a[1] % a[2])) % a[2]
result_3 = (a[0] * a[1]) % a[2]
result_4 = ((a[0] % a[2]) * (a[1] % a[2])) % a[2]

print(result_1,result_2,result_3,result_4)