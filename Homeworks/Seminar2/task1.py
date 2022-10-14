'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

from functions import inputFloat

n = inputFloat(1)
s = 0
for i in range(len(str(n))):
    e = str(n)[i]
    if e.isdigit():
        s += int(e)
print(f"Sum of digits in {n} is {s}.")