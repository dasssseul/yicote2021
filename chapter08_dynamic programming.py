
# [이코테 2021 강의 몰아보기]
# chapter08_dynamic programming

# 피보나치 함수(fibonacci Function)을 재귀함수로 구현

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))


# 피보나치 수열 : 탑다운 다이나믹 프로그래밍 소스코드

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0]*100

# 피보나티 함수를 재귀함수로 구현
def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제하면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


# 피보나치 수열 : 바텀업 다이나믹 프로그래밍 소스코드

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현(바텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])



# 실전 문제1. 개미 전사

# 답안 예시

# 정수 n을 입력 받기
n = int(input())

# 모든 식량 정보 입력 받기
k = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = k[0]
d[1] = max(k[0],k[1])

for i in range(2, n):
    d[i] = max(d[i-1],d[i-2]+k[i])

print(d[n-1])



# 실전 문제2. 1로 만들기

# 답안 예시

# 정수 x를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

# 다이나믹 프로그래밍 진행(바텀업)
# 함수 호출 횟수를 계산하기위해 1을 더해줌

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])



# 실전 문제3. 효율적인 화폐 구성

# 답안 예시

# 정수 n, m을 입력 받기
n, m = map(int, input().split())

# n개의 화폐 단위 정보를 입력 받기
coin = []
for i in range(n):
    coin.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 모두 계산 후에도 10001이라면 불가능 -> -1 출력
d = [10001] * (m+1)

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        # (j - coin[i])원을 만드는 방법이 존재하는 경우
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], d[j-coin[i]]+1)

# 최종적으로 m을 만드는 방법이 없는 경우
if d[m] == 10001:
    print(-1)
else:
    print(d[m])



# 실전 문제4. 금광
# 이해하는데 오~래 걸림

# 답안 예시

# 테스트 케이스 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))
    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(gold[index:index+m])
        index += m
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for x in range(n):
            # 왼쪽 위에서 오는 경우
            if x == 0:
                left_up = 0
            else:
                left_up = dp[x-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if x == n-1:
                left_down = 0
            else:
                left_down = dp[x+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[x][j-1]
            # 자기 자신 + 세 가지 경우 중 가장 큰 값
            dp[x][j] = dp[x][j] + max(left_up, left, left_down)
    result = 0
    # 마지막 열에 있는 수들 중 가장 큰 수 출력
    for k in range(n):
        result = max(result, dp[k][m-1])
    print(result)



# 실전 문제5. 병사 배치하기

# 답안 예시

n = int(input())
power = list(map(int, input().split()))

# 순서를 뒤집어 '최장 증가 부분 수열'(LIS) 문제로 변환
power.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0,i):
        if power[j] < power[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외해야하는 병사의 최소 수를 출력
print(n-max(dp))





