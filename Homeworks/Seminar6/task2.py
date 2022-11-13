'''Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
Пример:
- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37 }'''

from functions import inputFloat

n = inputFloat(1)

sum = float(0)

# s = {}
# for i in range(1, n + 1):
#     s[i] = round((1 + 1 / i) ** i, 2)
#     sum += s[i]

s = [0]
for i in range(1, n + 1):
    s.append(round((1 + 1 / i) ** i, 2))
    sum += s[i-1]

s = list(enumerate(s))
s.remove((0, 0))

print(f"Result is {s}")
print(f"Sum of elements: {sum}.")
