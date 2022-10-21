'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
import random

def rnd(fr, to):
    return random.randint(fr, to)

def superscript(n): # перевод в надстрочный формат
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def write_to_file(fn, text):
    f = open(fn, "w", encoding="UTF-8")
    f.writelines(text)
    f.close()

def create_polynomial_formula(k, fr, to):
    lst = [f"{rnd(fr, to)}*x{superscript(i)}" for i in reversed(range(2, k + 1))]
    #lst = [f"{rnd(fr, to)}*x^{i}" for i in reversed(range(2, k + 1))]
    x1 = rnd(fr, to)
    if x1 != 0:
        lst.append(f"{x1}x")
    x0 = rnd(fr, to)
    if x0 != 0:
        lst.append(str(x0))
    lst = " + ".join(lst)

    return lst + " = 0"

poly_f = create_polynomial_formula(16, 0, 100)

print(poly_f)
write_to_file("file.txt", poly_f)


