'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

from functions import inputFloat

n = inputFloat(0)

# for i in range(len(str(n))):
#     e = str(n)[i]
#     if e.isdigit():
#         s += int(e)

# оптимизация
sum_lst = (int(x) for x in str(n) if x.isdigit())
print(f"Sum of digits in {n} is {sum(sum_lst)}.")