A = int(input())

words = []

for i in range(A):
    words.append(input())

answer = 0  # 그룹 단어의 개수를 세기 위한 변수

for word in words:
    is_group_word = True
    for a in range(len(word) - 1):
        if word[a] != word[a + 1]:  # 인접한 문자가 다를 때
            if word[a] in word[a + 1:]:  # 현재 문자가 이후에 다시 등장하면
                is_group_word = False
                break  # 그룹 단어가 아니므로 중단
    if is_group_word:
        answer += 1  # 그룹 단어일 경우 카운트를 증가

print(answer)