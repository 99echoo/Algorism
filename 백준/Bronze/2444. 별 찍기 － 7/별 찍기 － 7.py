star = int(input())

# 증가하는 부분 출력
for i in range(star):
    print(' ' * (star - i - 1) + '*' * (2 * i + 1))

# 감소하는 부분 출력
for i in range(star - 2, -1, -1):
    print(' ' * (star - i - 1) + '*' * (2 * i + 1))
