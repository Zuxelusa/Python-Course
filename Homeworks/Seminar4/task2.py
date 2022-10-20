'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

#долгий способ - на больших числах долго думает
def prime_multipliers(n):
    # создаем список всех возможных делителей
    lst = [i for i in range(1, n + 1) if not n % i]

    #находим и удаляем из списка числа, также имеющих найденные простые множители
    for i in lst:
        for j in reversed(lst):
            if i != j and i !=1 and j !=1:
                if not j % i: lst.remove(j)
    return lst

print (prime_multipliers(12588))

#оказывается есть известный способ через деление. Работает быстрее
def prime_multipliers_by_division(n):
    div = 2
    lst = []
    while n > 1:
        if not n % div:
            n /= div
            lst.append(div)
        else:
            div += 1
    return sorted(list(set(lst)))

print(prime_multipliers_by_division(10245546512))
