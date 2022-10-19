'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

# это мой самый первый код на python, который я пытался написать, когда шел курс c#

N = int(input ("Введите число в 10-ом исчислении: "))
Calc = int(input ("Введите порядок исчисления (до 16 включительно): "))
TempN = N
Res = N
i = 0
Result = []

while (Res != 0):
    Res = Res // Calc
    tempInt = TempN - (Res * Calc)
    if tempInt == 10: tempInt = "a"
    if tempInt == 11: tempInt = "b"
    if tempInt == 12: tempInt = "c"
    if tempInt == 13: tempInt = "d"
    if tempInt == 14: tempInt = "e"
    if tempInt == 15: tempInt = "f"
    Result.append (tempInt)
    i += 1
    TempN = Res

i = 0
while (i < len(Result) // 2):
    temp = Result[i]
    Result[i] = Result [len(Result) - 1 - i]
    Result [len(Result) - 1 - i] = temp
    i += 1

# Выводим значение
print ('Число в', Calc, '-ом исчислении:', Result)