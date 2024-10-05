import sys
input = sys.stdin.read  # 빠른 입력을 위해 사용

# 입력을 받음
data = input().splitlines()
initial_string = data[0]
commands = data[2:]

# 커서의 왼쪽과 오른쪽 리스트
left_stack = list(initial_string)
right_stack = []

# 명령어 처리
for command in commands:
    if command == 'L':
        if left_stack:  # 왼쪽에 문자가 있다면
            right_stack.append(left_stack.pop())  # 왼쪽에서 하나 꺼내서 오른쪽에 추가
    elif command == 'D':
        if right_stack:  # 오른쪽에 문자가 있다면
            left_stack.append(right_stack.pop())  # 오른쪽에서 하나 꺼내서 왼쪽에 추가
    elif command == 'B':
        if left_stack:  # 왼쪽에 문자가 있다면
            left_stack.pop()  # 왼쪽에서 하나 삭제
    elif command.startswith('P'):
        _, char = command.split()  # 문자 추가 명령어 처리
        left_stack.append(char)

# 결과 출력
# 왼쪽 리스트와 오른쪽 리스트를 합침
print(''.join(left_stack + right_stack[::-1]))  # 오른쪽 리스트는 역순으로 붙여야 함