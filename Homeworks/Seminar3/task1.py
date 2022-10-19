'''Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''
from functions import *

def take_elements_from_indexes (lst: list, OddEVen: int = 0): #функция с парамтером выбора четных или нечетных позиций
    result_lst = []
    sum = 0
    for i in range(len(lst)):
        if i % 2 != OddEVen:
            result_lst.append(lst[i])
            sum += lst[i]
    return (result_lst, sum)

lst = create_new_list(9, 0, 9)

print(f"Source list: {lst}.")
result = take_elements_from_indexes(lst)
print (f"Result list: {result[0]}, суммой {result[1]}.")

