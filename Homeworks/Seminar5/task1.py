'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

def my_replace(text: str, excl: str):
    lst = [i for i in text.split() if excl not in i]
    return " ".join(lst)

text = "Привет, моя абвгдейка, привет абв! и ты туАБВда"
excl = "абв"
print(my_replace(text, excl))

