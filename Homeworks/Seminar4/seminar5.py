'''Задача 35.
В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

test_data = [
    ["3 4 5 6 7 9 10 11 12", 8],
    ["3 4 6 7 8 9 10 11 12", 5],
    ["1 3", 2]
]
for sequence, exp in test_data:
    find_missing(sequence) == exp
    # find_missing_func(sequence) == exp
'''

s = "3 4 5 6 7 9 10 11 12"
lst = s.split()
dif = lst[0]
for i in range(len(lst) - 1):
    if lst[i] == (lst[i+1] + dif):
        print(lst[i])
        break
'''
Задача 36. Дан список чисел.Создайте список, в который попадают
числа, описываемые возрастающую последовательность.Порядок элементов
менять нельзя. Пример:
[1, 5, 2, 3, 4, 6, 1, 7] = > [1, 5, 6, 7]

test_data = [
    [[1, 5, 2, 3, 4, 6, 1, 7], [1, 5, 6, 7]],
    [[1, 2, 3, 4, 6, 1, 7], [1, 2, 3, 4, 6, 7]]
]

for nums, exp in test_data:
    assert inc_sequence(nums) == exp

[1, 5, 6, 7]
[1, 2, 3, 4, 6, 7]
'''
lst = [1, 5, 2, 3, 4, 6, 1, 7]

lst2 = []
for i in range(0, len(lst)-1):
    for j in range(i, len(lst)):
        if lst[i] < lst[j]:
            lst2.append(lst[i])
            break


print(lst2)