import sys

#  반복문으로 여러줄 입력받는 상황에서는 반드시 sys.stdin.readline()을 사용해야 시간초과가 발생하지 않습니다.

# a = int(input())
# for i in range(a):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)


# 11021
# n = int(input())
# for i in range(1, n+1):
#     a, b = map(int, input().split())
#     print("Case #%d: %d" %(i, a+b))

# 2438
# *
# **
# ***
# ****
# *****
# n = int(input())
# for i in range(1, n+1):
#     print(i*"*")

# 2439
#     *
#    **
#   ***
#  ****
# *****
# n = int(input())
# for i in range(1, n+1): # 5부터 1까지
#     print(" " * (n-i) + "*"*i)


# 10871
# N, X = map(int, input().split())
# A = list(map(int, input().split()))
#
# for i in range(N):
#     if A[i] < X:
#         print(A[i], end=" ")


# 10952
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# while(True):
#     a, b = map(int, input().split())
#     if(a == 0 and b == 0):
#         break
#     print(a+b)


# 1110 사이클 문제

num = int(input())
check = num
new_num = 0
temp = 0
count = 0

while(True):
    # // 몫을 구하는 거 % 나머지
    # ex) 15 1+5 = 6
    temp = num//10 + num%10 # 주어진 수가 10보다 작다면 앞에 0을 붙이고
    # 5*10+4 54
    new_num = (num%10) * 10 + temp%10
    count += 1
    num = new_num
    if new_num == check:
        break

print(count)