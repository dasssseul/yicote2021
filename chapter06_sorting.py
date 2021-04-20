

# [이코테 2021 강의 몰아보기]
# chapter06_sorting


# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    # 가장 작은 원소의 인덱스
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    # 스와프
    array[i], array[min_index] = array[min_index], array[i]

print(array)



# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    for j in range(i, 0, -1):
        # 한 칸씩 왼쪽으로 이동
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break

print(array)



# 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # 피벗은 첫번째 원소
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # 엇갈렸다면 작은 데이터와 피멋을 교체
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


# 파이썬의 장점을 살린 퀵 정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    # 피벗은 첫 번째 원소
    pivot = array[0]
    # 피벗을 제외한 리스트
    tail = array[1:]

    # 분할된 왼쪽 부분
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

print(quick_sort_py(array))



# 계수 정렬

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

# 리스트에 기록된 정렬 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')



# 실전 문제1. 두 배열의 원소 교체

# 혼자 풀어보기

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(k):
    min_index = a.index(min(a))
    max_index = b.index(max(b))
    a[min_index], b[max_index] = b[max_index], a[min_index]

print(sum(a))


# 답안 예시

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 오름차순 정렬 수행
a.sort()
# 내림차순 정렬 수행
b.sort(reverse=True)

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    # A의 원소가 B의 원소보다 크거나 같을 때, 반복문 탈출
    else:
        break

print(sum(a))




