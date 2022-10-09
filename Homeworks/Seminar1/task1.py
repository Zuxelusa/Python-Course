'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
'''
def IsWeekDay(n):
    if 1 <= n <= 5: print("This is weekday!")
    elif 6 <= n <= 7: print("This is holiday!")
    else: print("This is not day of week!")

IsWeekDay(int(input("Input day of week: ")))
    
