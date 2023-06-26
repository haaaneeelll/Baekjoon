# 주사위 눈의 입력을 받습니다.
dice = input().split()

# 주사위 눈을 정수로 변환합니다.
dice = [int(x) for x in dice]

# 주사위 눈의 개수를 셉니다.
count = [0] * 7  # 1부터 6까지의 눈을 저장하는 리스트

for num in dice:
    count[num] += 1

# 상금 계산을 수행합니다.
prize = 0

if max(count) == 3:  # 같은 눈이 3개인 경우
    prize = 10000 + count.index(3) * 1000
elif max(count) == 2:  # 같은 눈이 2개인 경우
    prize = 1000 + count.index(2) * 100
else:  # 모두 다른 눈인 경우
    prize = max(dice) * 100

# 상금을 출력합니다.
print(prize)
