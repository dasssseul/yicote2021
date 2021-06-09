
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



