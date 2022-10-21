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
    print(f"The text was added to file '{fn}'.")

def create_polynomial_formula(k, fr, to):
    lst = [f"{rnd(fr, to)}*x{superscript(i)}" for i in reversed(range(2, k + 1))]

    # убирем все члены с 0 коэффициентом
    lst = list(filter(lambda i: i[:3] != "0*x", lst))

    # исключаем из отображения коэффициенты 1
    lst = list(map(lambda i: i.replace("1*x", "x"), lst))

    # добавляем член с Х в первой степени, если не 0
    x1 = rnd(fr, to)
    if x1 != 0: lst.append(f"{x1}x")

    # добавляем свободный член, если не 0
    x0 = rnd(fr, to)
    if x0 != 0: lst.append(str(x0))

    # собираем окончательный вид формулы
    lst = " + ".join(lst) + " = 0"

    return lst

k = int(input("K = "))
poly_f = create_polynomial_formula(k, 0, 100)

print(poly_f)
write_to_file("file.txt", f"k = {k}: {poly_f}")


