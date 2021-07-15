#로또 번호 6개 추첨하는 코드

# 1 . random 모듈을 가져오고
import random
# 2 . numbers 통을 만들고
numbers = range(1,46)
# 3 . 6개 입력을 받고
pick = random.sample(numbers,6)
# 4 . 출력
print(pick)