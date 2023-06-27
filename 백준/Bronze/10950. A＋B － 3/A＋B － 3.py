T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    A, B = map(int, input().split())  # A와 B를 입력받음
    result = A + B  # A와 B의 합을 계산
    print(result)  # 결과 출력
