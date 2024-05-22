alphabet = list(map(str,input()))


if len(alphabet) % 2 != 0:
    # 가운데 인덱스 계산
    middle_index = len(alphabet) // 2
    # 가운데 요소 제거
    alphabet.pop(middle_index)

error = 0
for i in range(len(alphabet) // 2) :
   if alphabet[i] != alphabet[-i-1] :
      error += 1

if error > 0 :
   print(0)
else:
   print(1)
