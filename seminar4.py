'''Задача 27
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
Пример
"12 346 62 34 9 25623 42 34" -> 25623, 9
 test_data = [
    ["12 346 62 34 9 25623 42 34", [25623, 9]],
    ["7 346 1 34 9 6 42 -2 6", [346, -2]],
]
for nums, expected in test_data:
    assert find_max_min(map(int, nums.split(" "))) == expected'''
'''
str_val = "12 346 62 34 9 25623 42 34"
str_tmp = str_val.split(" ")
max_val = int(str_tmp[0])
min_val = int(str_tmp[0])
for i in str_tmp:
    if int(i) < min_val:
        min_val = int(i)
    if int(i) > max_val:
        max_val = int(i)
print (str_val)
print (f"{max_val}, {min_val}")

for nums, expected in test_data:
    assert find_max_min(map(int, nums.split(" "))) == expected
'''
'''Задача 28
Найдите корни квадратного уравнения Ax² + Bx + C = 0, где A ≠ 0 двумя способами: 
1) с помощью математических формул нахождения корней квадратного уравнения 
2) с помощью дополнительных библиотек Python
test_data = [
    [[1, -3, 2], [1.0, 2.0]],
    [[1, 2, 1], [-1, -1]],
    [[2, 2, 1], []]
]
for nums, expected in test_data:
    assert quadratic_equation(*nums) == expected



def quadro_ecuat(nums_lst):
    a, b, c = nums_lst
    D = b**2 - 4 * a * c
    if D < 0: return []
    x1 = (-b + D**0.5) / (2 * a)
    x2 = (-b - D**0.5) / (2 * a)
    return [nums_lst, [x1, x2]]

print(quadro_ecuat([1, -3, 2]))
'''

'''Задача 29
Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
Теория
Наибольшим общим делителем (НОД) для двух целых чисел m и n называется наибольший из их общих делителей. Пример: для чисел 54 и 24 наибольший общий делитель равен 6. Наибольший общий делитель существует и однозначно определён, если хотя бы одно из чисел m или n не равно нулю.
Наименьшее общее кратное для нескольких чисел (НОК least common multiple) — это наименьшее натуральное число, которое делится на каждое из этих чисел.

test_data = [
    [[2, 3, 4, 5, 6], 60],
    [[16, 20], 80]'''

def find_NOK (a, b: float):
    delitel = min(a, b)
    while delitel > 2:
        if a % delitel == 0 and b % delitel == 0:
            break
        delitel /= 2
    return a * b / delitel

print (find_NOK(100, 80))