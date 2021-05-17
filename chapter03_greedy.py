
# [이코테 2021 강의 몰아보기]
# chapter03. greedy


# 예제 3-1. 거스름돈

n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    count += n // coin
    n %= coin

print(count)


# 문제1. 1이 될 때까지

# 혼자 생각해보기
n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n//k
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)


# 답안 예시1_로그 시간 복잡도

n, k = map(int, input().split())
result = 0

while True:
    target = (n//k) * k
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)


# 답안 예시2_단순 풀이

n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)


# 문제2. 곱하기 혹은 더하기

# 혼자 생각해보기

s = str(input())

result = int(s[0])

for i in s[1:]:
    if result == 0:
        result += int(i)
    elif int(i) == 1:
        result += int(i)
    else:
        result *= int(i)

print(result)


# 답안 예시

data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)


# 문제3. 모험가 길드

# 혼자 풀기

n = int(input())
scary = list(map(int, input().split()))
scary.sort()
group = 0
people = 1

for i in scary:
    if people >= i:
        group += 1
        people = 0
    else:
        people += 1
print(group)


# 답안 예시

n = int(input())
scary = list(map(int, input().split()))
scary.sort()

# 총 그룹의 수
group = 0

# 현재 그룹에 포함된 모험가의 수
people = 0

for i in scary:
    # 현재 그룹에 해당 모험가를 포함시키기
    people += 1
    if people >= i:
        group += 1
        people = 0

print(group)



# 실전 문제1. 큰 수의 법칙

# 혼자 풀어보기

n, m, k = map(int, input().split())
num = list(map(int, input().split()))
# 내림차순 정렬
num.sort(reverse=True)

# 가장 큰 수 2개가 같은 수라면, 중복 더하기 가능
if num[0] == num[1]:
    result = num[0] * m

# 다른 수라면, 한 세트로 묶어서 생각
else:
    set = num[0] * k + num[1]

    # 한 세트의 개수로 나눠진다면,
    if (m % (k + 1)) == 0:
        result = set * (m // (k + 1))
    else:
        result = set * (m // (k + 1)) + num[0] * (m % (k + 1))

print(result)


# 답안 예시

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
# 가장 큰 수 더하기
result += count * first
# 두번째로 큰 수 더하기
result += (m-count) * second

print(result)



# 실전 문제2. 숫자 카드 게임

# 혼자 풀어보기

n, m = map(int, input().split())
card = []
for i in range(n):
    number = list(map(int, input().split()))
    card.append(min(number))
print(max(card))


# 답안 예시
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)




# 그리디 알고리즘 복습

# 1번. 큰 수의 법칙

n, m, k = map(int,input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first = numbers[n-1]
second = numbers[n-2]

count = (m//(k+1))*k
count += m%(k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)



# 2번. 숫자 카드 게임

n, m = map(int, input().split())
value = 0

for _ in range(n):
    card = list(map(int, input().split()))
    min_value = min(card)
    value = max(value, min_value)

print(value)



# 3번. 1이 될 때까지

n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n%k == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)






