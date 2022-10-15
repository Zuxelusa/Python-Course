'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.'''

from functions import inputFloat
import random


def readFromLine(fn, l):
    f = open(fn, 'r')
    lines = f.readlines()
    return int(lines[l - 1])


n = inputFloat(1)

f = open("file.txt", 'w')
f.close()  # очистка файла

list = []
file = "file.txt"
m1 = 3  # указанная позиция для умножения
m2 = 5  # указанная позиция для умножения
for i in range(n):
    ns = random.randint(-n, n)
    list.append(ns)
    f = open(file, 'a')
    f.write(str(f"{ns}\n"))
    f.close()
print(list)
print(f"Multiply {list[m1 - 1]} and {list[m2 - 1]} is {readFromLine(file, m1) * readFromLine(file, m2)}.")
