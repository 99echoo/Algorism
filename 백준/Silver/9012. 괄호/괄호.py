def VPS():
    a = int(input())  # 테스트 케이스의 개수 입력
    for i in range(a):
        aa = input()  # 괄호 문자열 입력
        stack = []
        is_valid = True  # 올바른 VPS인지 확인하는 플래그
        
        for char in aa:
            if char == "(":
                stack.append(char)
            else:
                if stack:
                    stack.pop()  # 스택에서 '('를 꺼내서 짝을 맞춤
                else:
                    is_valid = False  # 스택이 비어있는데 ')'를 만난 경우
                    break
        
        # 괄호 문자열 처리가 끝난 후 스택이 비어있으면 올바른 VPS
        if is_valid and not stack:
            print("YES")
        else:
            print("NO")

VPS()