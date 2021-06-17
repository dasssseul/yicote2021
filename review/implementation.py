
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


# Q9. 문자열 압축

def solution(s):
    answer = len(s)
    # 1부터 문자열 길이의 절반까지 step을 설정
    for step in range(1,(len(s)//2)+1):
        # 문자열을 저장할 divided 초기화
        divided = ""
        # 맨 앞에서부터 step만큼의 문자열 추출
        previous = s[0:step]
        # previous 문자열의 길이 1로 초기화
        count = 1
        # step만큼 증가시킨 다음 문자열 추출을 위한 for문
        for i in range(step, len(s), step):
            # 이전의 문자열과 추출한 문자열이 같다면
            if previous == s[i:i+step]:
                # 문자열의 길이 +1
                count += 1
            # 다르다면
            else:
                # 길이가 2보다 크거나 같다면
                if count >= 2:
                    # divided에 문자열의 길이와 함께 이전 문자열 저장
                    divided += str(count) + previous 
                # 길이가 2보다 작다면(=1이라면)
                else:
                    # divided에 이전 문자열만 저장 (길이 저장 X)
                    divided += previous
                # 이전 문자열을 현재 추출한 문자열로 초기화
                previous = s[i:i+step]
                # 문자열의 길이 역시 초기화
                count = 1
        # 남은 문자열에 대한 처리 (위와 동일)
        if count >= 2:
            divided += str(count) + previous
        else:
            divided += previous
        # 만들어진 문자열 중 길이가 가장 짧은 경우로 answer 업데이트
        answer = min(answer, len(divided))
    return answer

