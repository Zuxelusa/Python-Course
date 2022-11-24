'''Создайте программу для игры в ""Крестики-нолики"".'''

from colorama import Fore, Back, Style

# проверка ввода данных
def inputcheck_xo(mes: str):
    while True:
        try:
            n = input(mes)
            #n = 11
        except ValueError:
            print("Нужно ввести число!")
        else:
            if str(n) in all_values: return str(n)
            else: print(f"Такого варианта нет!\n")

# функция поиска значения в списке сделанных ходов
def find_in_list(value: str, source: list):
    temp = -1
    for el in source:
        #if len(el) < 2:
        if el[1] == value:
            temp = el[0]
        #elif el == value: temp = value
    return temp

# вывод поля с заполнением значений
def matrix_output():
    for i in range(3):
        print("\t")
        for j in range(3):
            num = str(i)+str(j)
            ans = find_in_list(num, variants_set)
            if ans == "X" or ans == "O":
                # print(f"\t\033[36m {ans}", end="")
                print(Fore.CYAN + f"\t {ans}", end="")
            if ans == -1:
                print(Fore.RED + f"\t{num}", end="")
    print(f"\t", end="")
    print("\t")

# проверка окончания игры для одной комбинации
# возвращает bool при проверке выигрышного сочетания. отправляем сочетания из списка ('00', '01', '02'),
def check_for_win(ch_lst, variants_set):  # ('00', '01', '02')
    ch = False
    indicator = ""
    for i in range(len(ch_lst)): # для каждого значения из 3 делаем проверку
        val = find_in_list(ch_lst[i], variants_set)  # возвращает либо знак, либо -1, если нет значка
        if i == 0: indicator = val
        if val == -1: return False
        if indicator == val:
            indicator = val
            ch = True
        else: return False
    print("\t")
    return ch

# # проверка окончания игры для всех комбинаций
def check_for_win_total (var_set):
    for i in check_lst:
        if check_for_win(i, var_set): return True
    return False

# запрос хода с проверкой, есть ли уже ход на этом значении ?
def input_step(cat: str):
    while True:
        print("\t")
        val = inputcheck_xo(f"Куда поставить {cat} ? ")
        val_result = find_in_list(val, variants_set)
        if val_result == -1:
            print("\t")
            variants_set.append((cat, val))
            break
        else:
            print("Место занято")

# таблица проверки на выигрышные события
check_lst = [
    ('00', '01', '02'),
    ('10', '11', '12'),
    ('20', '21', '22'),
    ('00', '10', '20'),
    ('01', '11', '21'),
    ('02', '12', '22'),
    ('00', '11', '22'),
    ('20', '11', '02')
]
symbols = ['X', 'O']
all_values = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
variants_set = []

print("\n")
print(Back.BLUE + f"Начинаем игру в крестики-нолики!")
print(Style.RESET_ALL)

step = 0
matrix_output()

while True:
    input_step(symbols[step])
    matrix_output()

    if step == 0: step = 1
    else: step = 0

    if check_for_win_total(variants_set):
        print("Winner!")
        break

