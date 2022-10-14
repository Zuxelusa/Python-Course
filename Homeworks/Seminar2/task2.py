'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)'''

from functions import inputFloat

n = inputFloat(1) # запрос int

list = [1]
for i in range(1, n):
    list.append(list[i - 1] * (i+1))
print(list)