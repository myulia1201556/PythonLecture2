# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число.

import random

print('Введите число элементов в списке N: ')
N = int (input())
arr = []

for _ in range(N):
    arr.append(random.randint(-N, N))
print(arr)

x = []
with open("file.txt", "r") as data:
   x = data.read().split("\n")
result = arr[int(x[0])] * arr[int(x[1])]

print(result)

