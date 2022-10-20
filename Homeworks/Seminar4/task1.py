'''Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$'''
import math

# функция, которая выводит число Pi, параметр функции - это вывод с точностью n знаков после запятой.
# При значении n > 7, функция очень долго выполняется.
def Pi(n):
    x = 1
    for i in range(2, 10**(n + 1), 2):
        x = x * (i / (i + 1)) * ((i + 2)/(i + 1))
    return  round(4 * x, n)

#3,1415926535

print(Pi(3))

print(math.pi)


