
#выбрать четные и составить список пар (число; квадрат числа)

f = open("file.txt", 'r')
lst = map(int, f.readline().split())
f.close()
result = [(i, i**2) for i in lst if i % 2 == 0]
print(list(lst))
print(result)