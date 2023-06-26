# 현재 시각 입력 받기
current_hour, current_minute = map(int, input().split())

# 오븐구이에 필요한 시간 입력 받기
cooking_time = int(input())

# 현재 시각에 오븐구이에 필요한 시간을 더해줌
end_hour = (current_hour + (current_minute + cooking_time) // 60) % 24
end_minute = (current_minute + cooking_time) % 60

# 오븐구이가 끝나는 시각 출력
print(end_hour, end_minute)
