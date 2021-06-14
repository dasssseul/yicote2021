
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




# Q5. 볼링공 고르기 

# 나의 풀이

# 볼링공의 개수와 최대 무게 입력 받기
n, m = map(int, input().split())

# 볼링공의 무게 입력 받기
weight = list(map(int, input().split()))

# 서로 다른 공을 골라서 묶어줄 배열 초기화
balls = []

for i in range(n):
    for j in range(i+1, n):
        # i번째 공의 무게와 j번째 공의 무게가 다를 경우에만, balls에 추가
        if weight[i] != weight[j]:
            balls.append((weight[i], weight[j]))
        # 같은 경우 다음으로 넘어가기
        else:
            continue

# balls에 포함된 조합의 길이 출력
print(len(balls))



# Q5. 볼링공 고르기 

# 책의 풀이

# 볼링공의 개수와 최대 무게 입력 받기
n, m = map(int, input().split())

# 볼링공의 무게 입력 받기
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for i in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[i] += 1

result = 0

# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    # 무게가 i인 볼링공의 개수 제외
    n -= array[i]
    # 무게가 i인 볼링공이 선택할 수 있는 경우의 수와 곱하기
    result += array[i] * n


print(result)



# Q6. 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    if sum(food_times) <= k:
        return -1

    q = []
    # 시간이 작은 음식부터 빼야하기 때문에
    # 입력받은 food_times를 (음식 시간, 음식 번호) 튜플 형태로 우선순위 큐에 삽입
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    # 먹기 위해 사용한 시간
    sum_value = 0

    # 직전에 다 먹은 음식의 시간 
    previous = 0

    # 남은 음식의 개수
    length = len(food_times)

    while sum_value + (q[0][0] - previous) * length <= k:
        # 현재 큐에서 가장 적게 걸리는 음식의 시간 꺼내기
        now = heapq.heappop(q)[0]
        # 먹기 위해 사용한 시간 += (현재 음식의 시간 - 직전에 다 먹은 음식의 시간) * 남은 음식의 개수
        sum_value += (now - previous) * length
        # 현재의 음식을 다 먹었으므로 남은 음식의 수 -1
        length -= 1
        # 직전에 다 먹은 음식의 시간 업데이트
        previous = now
    
    # 남은 음식 중에 몇 번째 음식인지 확인하기 위해 
    result = sorted(q, key = lambda x : x[1]) # 음식 번호 순으로 정렬
    return result[(k-sum_value)%length][1] # 남은 시간을 남은 음식의 개수로 나눈 나머지를 이용해 출력

# 결과 확인
print(solution([3, 1, 2], 5))  





