# [이코테 2021 강의 몰아보기]
# 1.코딩 테스트 출제 경향 분석 및 파이썬 문법 부수기


# 리스트 컴프리헨션
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N x M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0]*m for i in range(n)]
print(array)

# 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_) 사용
for _ in range(5):
    print("hello World")

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형
result = [i for i in a if i not in remove_set]
print(result)


# 집합 자료형
# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)


# 기본 입출력
# 빠르게 입력받기
import sys
data = sys.stdin.readline().rstrip()
print(data)


# 함수
# global키워드
a = 0

def func():
    # 함수 바깥에 선언된 a를 바로 참
    global a
    a += 1

for i in range(10):
    func()

print(a)


# 람다 표현식
# 일반적인 add 함수 사용
def add(a,b):
    return a+b

print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a+b)(3,7))

# 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50),('이순신', 32),('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))


# 자주 사용되는 표준 라이브러리
# 순열과 조합
# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 조합
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

# 중복 순열
from itertools import product

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기 (중복 허용)
result = list(product(data, repeat=2))
print(result)

# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기(중복 허용)
result = list(combinations_with_replacement(data, 2))
print(result)

# 등장 횟수를 세는 기능_Couter
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(dict(counter))

# 최대 공약수와 최소 공배수
import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a,b)
a = 21
b = 14

print(math.gcd(21, 14))
print(lcm(21, 14))


























