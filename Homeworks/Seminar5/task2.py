'''Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""'''
import random
from time import sleep

# проверка ввода данных
def inputcheck(mes: str, rng_from: int, rng_to: int):
    while True:
        try:
            n = int(input(mes))
        except ValueError:
            print("Нужно ввести число!")
        else:
            if rng_from <= n < rng_to + 1: return int(n)
            else: print(f"Нужно значение от {rng_from} до {rng_to}\n")

# жребий
def su_e_fa():
    while True:
        variants = {
            0: "КАМЕНЬ",
            1: "НОЖНИЦЫ",
            2: "БУМАГА"
        }
        print("Определим, кто ходит первым на 'Камень-Ножницы-Бумага'. ", end="")
        sleep(0.5)
        print("Раз! ", end="")
        sleep(0.5)
        print("Два! ", end="")
        sleep(0.5)
        print("Три! ")
        bot = random.randint(0, 2)
        user = input("Что вы показали ? (0 - к, 1 - н, 2 - б) ")
        if user.isdigit():
            user = int(user)
            if 0 <= user < 3:
                print(f"У меня {variants[bot]},у тебя {variants[user]}.")
                if bot == user:
                    print("Ничья!")
                    print("Сыграем еще раз!")
                else:
                    if (bot == 0 and user == 1) or (bot == 1 and user == 2) or (bot == 2 and user == 0):
                        print("Я выиграл!")
                        return -1
                    else:
                        print("Ты выиграл!")
                        return 1
            else:
                print("Нужно ввести 0 или 1 или 2.")
        else:
            print("Не понял вас...")
            True

# процедура хода игрока (для бота и для игрока)
def input_player(limit: int, total: int,  player):
    if player == 0:
        cur = random.randint(1, min(total - 1, limit))
        print (f"Я забираю {cur} конфет!")
        return cur
    else:
        return inputcheck("Сколько конфет забираете: ", 1, min(total - 1, limit))

#о снвная игра
def candy_game(total: int, limit: int = 28):

    print(f"\tНачинаем игру c конфетами. Кто возьмет последним, тот проиграл. \n "
      f"Брать можно не более чем {limit} конфет за ход. Всего на столе {total} конфет. \n")

    # определяем второго игрока: бот или юзер
    player_type = inputcheck("Выберите режим игры: с ботом (0) или с другом(1): ", 0, 1)

    if player_type == 0:
        #определить первый ход жребием
        print(f"Но сначала ...")
        step = su_e_fa()
        if step == 1: print(f"Ходи первым!")

    if player_type == 1:
        step = -1
        if inputcheck(f"Кто ходит первым? (1 или 2): ", 1, 2) == 1: step = 1

    print(f"Начинаем игру! У нас на столе {total} конфет.")

    # запускаем цикл проверки окончания конфет
    while total > 1:
        # процедура хода игрока 1
        if step == 1:
            print(f"Ваш ход!")
            cur = inputcheck("Сколько конфет забираете: ", 1, min(total - 1, limit))
            total -= cur

        # процедура хода игрока 2 или бота
        if step == -1:
            print(f"Ход второго игрока!")
            total -= input_player(limit, total, player_type)

        step *= -1
        print(f"Сейчас на столе {total} конфет(ы).\n")

    # проверка результата
    if step == 1:
        print ("Я выиграл!")
    if step == -1:
        print ("Ты выиграл!")

candy_game(221, 28)






