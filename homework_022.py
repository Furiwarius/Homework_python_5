# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def mode_selection():
    
    while True:
        print("1 - PvP на одном компьютере\n2 - PvE")
        new_input = input("Выберете режим: ")
        if new_input=='1' or new_input=='2':
            return int((new_input))
        else: 
            continue


def input_processing():
    
    while True:
        try:
            new_input = abs(int(input("Введите количество конфет, которое хотите взять: ")))
        except ValueError:
            print("То, что вы ввели, не подойдет. Попробуйте снова")
            continue
        if new_input>28 or new_input==0:
            print("Количество конфет должно быть не больше 28 и не равно 0")
            continue
        return new_input


def game_against_computer(candy):

    if candy<=28:
        return candy
    else:
        numbers = [val for val in range(1, 28)]
        for num in numbers:
            if  candy-num-28==30:
                return num
            elif candy-num==29:
                return num
    return 28


def mode_PvP():

    candy = 2021
    player_1 = 0
    player_2 = 0
    whose_move = randint(0, 1)

    while True:
        print("------------------------------------------")
        print(f"Количество конфет: {candy}")
        print(f"Количество конфет Player 1: {player_1}")
        print(f"Количество конфет Player 2: {player_2}")

        if whose_move==0:
            print("Ход игрока Player 1")
            candies = input_processing()
            player_1+=candies
        else:
            print("Ход игрока Player 2")
            candies = input_processing()
            player_2+=candies

        if candy-candies<=0:
            print(f"Player {whose_move+1} победил")
            break
        else:
            candy-=candies
            whose_move = not whose_move
        

def mode_PvE():

    candy = 2021
    player_1 = 0
    Computer = 0
    whose_move = randint(0, 1)

    while True:
        print("------------------------------------------")
        print(f"Количество конфет: {candy}")
        print(f"Количество конфет Player 1: {player_1}")
        print(f"Количество конфет Computer: {Computer}")

        if whose_move==0:
            print("Ход игрока Player 1")
            candies = input_processing()
            player_1+=candies
        else:
            print("Ход Computer")
            candies = game_against_computer(candy)
            Computer+=candies

        if candy-candies<=0:
            if whose_move==0:
                print("Player 1 победил")
                break
            else:
                print("Computer победил")
                break
        else:
            candy-=candies
            whose_move = not whose_move
                

mode = mode_selection()

if mode==1:
    mode_PvP()
else:
    mode_PvE()