# https://www.acmicpc.net/problem/10869
import math
A, B = input().split()

print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)//int(B)) # /는 실수, //는 정수
#print(math.floor(int(A)/int(B)))
print(int(A)%int(B))
