
# [이코테 2021 강의 몰아보기]
# chapter07_binary search


# 이진 탐색 소스 코드 구현(재귀 함수)

def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end)//2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)



# 이진 탐색 소스코드 구현(반복문)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid - 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))

# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)



# 파이썬 이진 탐색 라이브러리

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4


# 값이 특정 범위에 속하는 데이터 개수 구하기

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터의 개수 출력
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))



# 실전 문제 1. 떡볶이 떡 만들기

# 혼자 풀어보기

# 주의 : 선형 탐색으로 시간 초과 판정을 받을 수 있다

n, m = map(int, input().split())
tteok = list(map(int, input().split()))
max_h = 0

for i in range(max(tteok)+1):
    result = []
    for k in tteok:
        if k <= i:
            result.append(0)
        else:
            result.append(k-i)
    if i > max_h and sum(result) >= m:
        max_h = i

print(max_h)


# 답안 예시

n, m = map(int, input().split())
tteok = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(tteok)

# 이진 탐색 수행(반복문)
result = 0
while (start <= end):
    total = 0
    mid = (start+end)//2
    for i in tteok:
        # 잘랐을 때의 떡의 양 계산
        if i > mid:
            total += i - mid
    # 떡의 양이 부족한 경우 왼쪽 부분 탐색
    if total < m:
        end = mid - 1
    # 떡의 양이 넘치는 경우 오른쪽 부분 탐색
    else:
         # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        result = mid
        start = mid + 1

print(result)



# 실전 문제 2. 정렬된 배열에서 특정 수의 개수 구하기

# 혼자 풀어보기

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)

print(right_index - left_index)


# 답안 예시

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)


