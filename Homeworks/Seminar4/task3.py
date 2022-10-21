'''Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности.'''

import random

lst = [random.randint(0, 15) for i in range(51)]
print(f"Source list: {lst}.")
print(f"Result list: {set(lst)}.")