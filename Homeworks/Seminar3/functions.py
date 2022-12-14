
import random
def inputFloat(t = 0):# 0 - float, 1 - int
    while True:
        if t == 0: n = input("Input real number: ")
        if t == 1: n = input("Input integer number: ")
        try:
            if t == 0: return float(n)
            if t == 1: return int(n)
        except ValueError:
            print("Try again!")

def create_new_list (quantity, start, end):
    lst = []
    for i in range(quantity):
        lst.append(random.randint(start, end))
    return lst