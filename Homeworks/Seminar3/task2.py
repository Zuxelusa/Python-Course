'''Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

from functions import *
import math

lst = create_new_list(9, 10, 99)

lst_result = []
for i in range(math.ceil((len(lst) / 2))):
    lst_result.append(lst[i] + lst[-i - 1])

print(lst)
print(lst_result)