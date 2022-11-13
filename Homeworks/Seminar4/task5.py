'''Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.'''
def file_read_line(fn):
    f = open(fn, "r", encoding="UTF-8")
    line = f.readline()
    f.close
    return line
def el_split_for_x(el: str, n: int):
    if "x" in el:
        if n == 0:
            return int(el.split("x")[0].replace("*", ""))
        if n == 1:
            if type(el.split("x")[1]) == str: return 1
            else:
                return el.split("x")[1].translate(regular)
    else: return int(el)
def line_replace_and_list(line):
    line = line.split(": ")[1]
    line = line.split(" =")[0]
    line = line.replace("*", "")
    return line.split(" + ")

#функция, возвращающая выборку из всех элементов с 2 параметрами, либо в степени 1 и без x
def list_to_operate(total_tuple, n = 0):
    result = []
    for i in total_tuple:
        if n == 1:
            if (len(i) > 1 and i[1] == "") or len(i) == 1:
                result.append(i)
        else:
            if len(i) > 1 and i[1] != "":
                result.append(i)
    return result

regular = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
regular_back = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

line0 = (file_read_line("file.txt"))
line1 =(file_read_line("file1.txt"))

l0_lst = line_replace_and_list(line0)
l1_lst = line_replace_and_list(line1)

# находим максимальную степень двух полиномов
max_st = 0
for i in l0_lst + l1_lst:
        cur = int(el_split_for_x(i, 1))
        if cur > max_st: max_st = cur

# переводим в список кортежей, в которых 0 - кэфф., 1 - степень
total_tuple = []
for i in l0_lst + l1_lst:
    i = i.translate(regular)
    total_tuple.append(i.split("x"))

part1 = list_to_operate(total_tuple, 0)
part2 = list_to_operate(total_tuple, 1)

def sum_in_tuple(lst: list):
    s = 0
    for i in lst:
        s += int(i[0])
    return [s, lst[0][1]]

#собираем первую часть полинома с коэффициентами от K до 2
new_lst = []
for i in reversed(range(2, max_st + 1)):
    temp_lst = list(filter(lambda x: int(x[1]) == i, part1))
    new_lst.append(sum_in_tuple(temp_lst))

new_lst = list(map(lambda x: str(x[0]) + "*x" + str(x[1]).translate(regular_back), new_lst))

x1 = [i for i in part2 if len(i) == 2]
x0 = [i for i in part2 if len(i) == 1]
def sum_in_tuple2(lst: list):
    s = 0
    for i in lst:
        s += int(i[0])
    return s

new_lst.append (str(sum_in_tuple2(x1)) + "x")
new_lst.append (str(sum_in_tuple2(x0)))

result_polynom = f"k = {max_st}: " + " + ".join(new_lst) + " = 0"

print(file_read_line("file.txt"))
print(file_read_line("file1.txt"))
print(result_polynom)

f = open("result.txt", "w", encoding="UTF-8")
f.write(result_polynom)
f.close()


