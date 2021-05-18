
# [이코테 2021 강의 몰아보기]
# chapter04_implementation


# 예제 4-1. 상하좌우

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


# 예제4-2. 시각

n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)



# 실전 문제 1. 왕실의 나이트

# 혼자 풀어보기

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

night = input()
x = ord(night[0])
y = int(night[1])
count = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if (ord('a') <= nx <= ord('h')) and (1 <= ny <= 8):
        count += 1
        nx, ny = x, y

print(count)


# 답안 예시

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)



# 예제 4-3. 문자열 재정렬

# 혼자 풀어보기
word = input()
number = []
alphabet = []
result = 0
for i in range(10):
    number.append(str(i))

for i in word:
    if i in number:
        result += int(i)
    else:
        alphabet.append(ord(i))
alphabet.sort()

for i in alphabet:
    print(chr(i),end="")
print(result)


# 답안 예시
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳 오름차순 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))



# 실전 문제 2. 게임 개발

# 답안 예시
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 방문한 곳을 표시할 리스트 초기화
mymap = [m*[0] for _ in range(n)]
mymap[x][y] = 1

# 북, 동, 남, 서 방향 벡터 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 육지와 바다를 array 리스트에 입력받기
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 왼쪽 회전 함수 정의
# 북 0, 동 1, 남 2, 서 3
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 방문 가능 경우의 수 cnt
# 회전 횟수 turn_time
cnt = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 방문한 적이 없고, 육지라면 이동
    if mymap[nx][ny] == 0 and array[nx][ny] == 0:
        mymap[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    # 그 외의 경우에는 회전 횟수 증가
    else:
        turn_time += 1
    # 네 방향 모두 이미 갔거나, 바다로 되어있다면
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 한 칸 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤도 바다라면 브레이크
        else:
            break
        turn_time = 0

print(cnt)



# 구현 알고리즘 복습

# 1번. 상하좌우

n = int(input())
plans = input().split()

x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)



# 2번. 시각

n = int(input())
cnt = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)



# 3번. 왕실의 나이트

input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

cnt = 0

for step in steps:
    next_row = row + step[1]
    next_column = column + step[0]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        cnt += 1

print(cnt)



# 4번. 게임개발

n, m = map(int,input().split())

x, y, direction = map(int, input().split())

# 방문 처리를 위한 맵
d = [[0]*m for _ in range(n)]
# 현재 위치 방문 처리
d[x][y] = 1

# 육지, 바다 맵 정보
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 이동에 따른 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향 회전 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 방문한 칸, 회전 횟수 세기
cnt = 1
turn_time = 0

# 이동 구현

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        x, y = nx, ny
        d[nx][ny] = 1
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)







