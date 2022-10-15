'''Реализуйте алгоритм перемешивания списка.'''

from functions import *

def my_shuffle(lst):
    for i in range(len(lst)):
        rnd_pos = random.randint(0, len(lst) - 1)
        temp = lst[rnd_pos]
        lst[rnd_pos] = lst[i]
        lst[i] = temp
    return lst

lst = create_new_list(8, -9, 9)

print(f"List: {lst}")
print(f"Shuffled list: {my_shuffle(lst)}")