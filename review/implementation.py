
# [이코테]알고리즘 유형별 기출문제 풀이
# 구현

# Q7. 럭키 스트레이트
# 백준 18406번 문제와 동일

# 나의 풀이 

# 점수 입력 받기
n = int(input())
# 입력받은 점수를 문자열로 변환
n = str(n)

score = []
# 문자 하나씩 정수형으로 변환해 score에 삽입
for i in n:
    score.append(int(i))

# 중간 인덱스 값 구해주기
half = int(len(n)/2)

# 슬라이싱을 이용해 왼쪽 절반의 합과 오른쪽 절반의 합 비교
if sum(score[:half]) == sum(score[half:]):
    print("LUCKY")
else:
    print("READY")


# 책의 풀이

# 점수 입력받기
n = input()

# 점수값의 총 자릿수 세기
length = len(n)

summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    summary -= int(n[i])

# 양쪽의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")


# Q8. 문자열 재정렬

# 나의 풀이 

# 문자열 입력 받기
s = input()

# 숫자를 골라내기 위한 number 리스트 정의
number = [str(i) for i in range(10)]

word = []
result = 0
cnt = 0

for i in s:
    # 숫자일 경우 합 구해주기
    if i in number:
        cnt += 1
        result += int(i)
    # 아닐 경우 word에 삽입
    else:
        word.append(i)

# 알파벳 오름차순 정렬
word.sort()

# 숫자의 합 삽입해주기
if cnt != 0:
    word.append(result)

# 최종 결과 출력
for i in word:
    print(i, end="")


# 책의 풀이_isalpha

data = input()
result = []
value = 0
cnt = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 개수 세기, 합 계산
    else:
        cnt += 1
        value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 책의 경우 value != 0일 때로 조건을 세웠으나,
# 위처럼 조건을 세웠을 경우 숫자에 0이 입력됐을 때도 출력을 안해주는 오류 발생
# 따라서, 나는 숫자의 개수를 세주는 cnt != 0일 때로 조건을 세웠다
if cnt != 0:
    result.append(str(value))

# 최종 결과 출력(join 함수)
print(''.join(result))

