
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


# 문제3. 모험가 길

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



