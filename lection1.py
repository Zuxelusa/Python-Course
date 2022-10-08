"""
Задача 1.
Написать программу, которая принимает на вход два целых числа и проверяет,
является ли одно число квадратом другого.
Примеры
5, 25 -> да
4, 16 -> да
25, 5 -> да
8,9 -> нет

"""
"""
a = int(input("Input a:"))
b = int(input("Input b:"))
if (a * a == b) or (b * b == a):
    print("Yes!")
else:
    print ("No!")
"""
"""

1. Понять смысл задания
2. Разбираемся с вх. вых. данными
3. Алгоритм своими словами (псевдокод)
4. Записать код
5. Проверить
6. Улучшить код (рефакторинг)
7*. Оптимизация (зависит от требований к задаче)
"""
"""
    a = int(input("a - "))
    b = int(input("b - "))
    if a == 0 or b == a:
        break
    if a * a == b or b * b ==a:
        print("Да")
    else:
        print("Нет")

print("Работа программы завершена.")
"""
"""
Задача 2.
Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
Примеры:
1, 4, 8, 7, 5 -> 8
78, 55, 36, 90, 2 -> 90
"""
def CreateCustomArray (n):
    list = []
    for i in range(n):
        list.append(int(input(f"Input {i + 1} element: ")))
    return list

def CreateRandomArray (n, fr, to):
    import random
    list = []
    for i in range(n):
        list.append(random.randint(fr, to + 1))
    return list

def FindMax (arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max: max = arr[i]
    return max
"""
n = int(input("Input size of array: "))
fr = int(input("From: "))
to = int(input("To: "))
array = CreateRandomArray(n, fr, to)
print(array)
print(f" Максимальное число: {FindMax(array)}.")
"""
"""
Задача 3.
Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
Примеры:
5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""
"""
n = int(input("Input N: "))
for i in range(-n, n + 1): print(f"{i} ", end="")
"""
"""
Задача 4.
Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
"""
"""
n = int(input("Input N: "))
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0: 
    print ("Yes!") 
else: 
    print ("No!")
"""
"""
Задача 5.
Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
Примеры
6.78 -> 7
5 -> нет
0.34 -> 3
"""

n = float(input("Input N: "))
print(f"The first symbol after dot is {int(n * 10 % 10)}")


