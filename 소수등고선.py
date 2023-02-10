'''
여러분은 배열크기 N과 시작위치 X , Y와 소수의 범위 a, b를 입력받아 숫자등고선을 만들어야 합니다!!
예를 들어 배열크기가 5, 시작위치가 3, 4이고, 배열 N 안에 들어갈 수 있는 소수의 범위가 4, 30 일때 
3, 4로 시작하는 다음과 같은 숫자등고선을 만들수 있습니다. (소수 범위 안에서 가장 작은 소수부터 배열 안을 모두 채울때까지 소수를 증가시키면서 채웁니다)

배열 N의 범위는 1<=N<=120 이며 좌표값 X,Y는 배열 크기보다 같거나 작다.
그리고 a,b의 범위는 2<=a<b<=2000이다.

<input>
N = 5, X = 3, Y = 4, a = 4, b = 30

<output>
19 17 13 11 13
17 13 11 7 11
13 11 7 5 7
17 13 11 7 11
19 17 13 11 13
'''

import math

#소수인지 확인하는 함수
def check_num(num):
    while(num != calculate_num(num)):
        num = calculate_num(num)
    return num

def calculate_num(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            num += 1
            break 
    return num


# 입력값 받기
N = int(input())
X, Y = map(int, input().split())
a, b = map(int, input().split())

#범위 안에서의 가장 작은 소수로 첫 배열 선언
a = check_num(a)
array = [[a for col in range(N)] for row in range(N)]

#좌표값(X,Y)를 기준으로 배열 채우기
for index in range(N):
    gap = abs((Y-1) - index)
    if gap != 0: 
        new_num = a       
        for i in range(gap):   
            new_num = check_num(new_num+1)
        array[X-1][index] = new_num
    else:
        array[X-1][index] = a

for col in range(N):
    for row in range(N):
        gap = abs((X-1) - row)
        if gap != 0: 
            value = array[X-1][col]       
            for i in range(gap):   
                value = check_num(value+1)
            array[row][col] = value
        else:
            pass

# 배열 확인
for i in array :
    for j in i:
        print(j,end=" ")
    print()