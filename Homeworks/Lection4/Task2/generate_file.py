import random
import string

def generate_field(str_type, length): # 1 - одно слово, 2 - число, 3 - ФИО
    if str_type == 1: return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    if str_type == 2: return ''.join(random.choice(string.digits) for i in range(length))
    if str_type == 3:
        lst = []
        for i in range(3):
            lst.append(''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(length - 2, length + 2))))
    return " ".join(lst)

def generate_file(file, length): #генерирует файл с указанным количеством строк
    title = f"ID\tFIO\tAddress\tPhone number\t Phone number 2\n"
    with open(file, "w") as f:
        f.writelines(title)
        for i in range(length):
            f.writelines(f"{i}\t{generate_field(3, 7)}\t{generate_field(1, 30)}\t{generate_field(2, 11)}\t{generate_field(2, 11)}\n\n")

