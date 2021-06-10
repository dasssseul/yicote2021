
# [이코테]알고리즘 유형별 기출문제 풀이
# 그리디 알고리즘


# Q1. 모험가 길드

# 모험가의 수, 공포도 입력 받기 
n = int(input())
scary = list(map(int, input().split()))

# 공포도 오름차순 정렬
scary.sort()

# 그룹과 사람의 수 초기화
group = 0
people = 0

for i in scary:
    # 자기 자신 people에 포함
    people += 1
    # 공포도보다 people의 수가 크거나 같다면
    if people >= i:
        # 그룹으로 묶어 세주고
        group += 1
        # people은 초기화
        people = 0

# 그룹의 수 출력
print(group)



# Q2. 곱하기 혹은 더하기

# 문자열 입력 받기
numbers = input()

# 최댓값 첫번째 수로 초기화
result = int(numbers[0])

# 첫번째 수 제외하고 for문
for i in numbers[1:]:
    # 결과가 0이거나 1이면 더하기
    if result == 0 or result == 1:
        result += int(i)
    # 아니면 곱하기해서 최댓값 구하기
    else:
        result *= int(i)

print(result)



# Q3. 문자열 뒤집기
# 백준 1439번 문제와 동일

# 문자열 입력받기
s = input()

# 전부 0으로 바꾸는 경우
count0 = 0

# 전부 1로 바꾸는 경우 
count1 = 0

# 첫 번째 원소에 대해서 처리
if s[0] == '0':
    count1 += 1
else:
    count0 += 1

# 두 번째 원소부터 모든 원소를 확인하면서
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        # 다음 수가 0일 경우 1로 바꿔줘야하기 때문에 count1 + 1
        if s[i+1] == '0':
            count1 += 1
        # 다음 수가 1일 경우 0으로 바꿔줘야하기 때문에 count0 + 1
        else:
            count0 += 1

# 뒤집는 횟수의 최솟값 출력
print(min(count0, count1))



# Q4. 만들 수 없는 금액
# 백준 2437번. 저울 문제와 비슷한 유형

# 동전의 개수 입력 받기
n = int(input())

# 회폐의 단위 입력 받기
coin = list(map(int, input().split()))

# 화폐 단위 오름차순 정렬
coin.sort()

# 더해서 만들 수 있는지 확인할 타켓 설정
target = 1


for i in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < i:
        break
    target += i

print(target)






