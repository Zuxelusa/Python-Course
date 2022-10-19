'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.
Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

def take_fract_part(n: float, r = 3):
    return round(n - int(n), r)

lst = [1.1, 1.3, 3.1, 5, 10.005]

max_val = take_fract_part(lst[0])
min_val = max_val

for el in map(float, lst):
    current = take_fract_part(el)
    if current != 0:
        if current > max_val: max_val = current
        if current < min_val: min_val = current

print(max_val - min_val)