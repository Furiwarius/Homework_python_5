# Создайте программу для игры в ""Крестики-нолики"".

from random import randint

import os


def input_processing(positions):
    
    while True:
        new_input = input("Введите позицию, которую хотите занять: ")
        if new_input.isdigit():
            if new_input in positions:
                return new_input
            else: 
                print("Вы ввели неправильный номер позиции или эта позиция уже занята")
                continue
        else:
            print("То, что вы ввели, не подойдет. Попробуйте снова")
            continue


def search_matches(pos_list, vin_position):
    for vin_list in vin_position:
        meter=0
        for i in pos_list:
            if i in vin_list:meter+=1
        if meter==3: return 1
        else: meter=0
    else:
        return -1


def victory_check(field, vin_position):
    x_pos = []
    o_pos = []

    for i, line in enumerate(field):
        for n, column in enumerate(line):
            if column=='X':
                x_pos.append([i, n])
            elif column=='O':
                o_pos.append([i, n])

    for n, value in enumerate([x_pos, o_pos], 1):
        if search_matches(value, vin_position)!=-1:
            return n
    else: return -1


def conclusion(field):
    for i in field:
        print(' | '.join(i))
        print('----------')


def mode_PvP():

    whose_move = randint(0, 1)
    field = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]

    positions = {}
    for i, line in enumerate(field):
        for j, column in enumerate(line):
            positions[column] = [i, j]

    vin_position = []
    for i in range(3):
        vin_position.append([[i, n] for n in range(3)])
        vin_position.append([[n, i] for n in range(3)])
    else: 
        vin_position.append([[i,i] for i in range(3)])
        vin_position.append([[0,2], [1,1], [2,0]]) # не придумал как это сгенерировать


    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        conclusion(field)

        if whose_move==0:
            print("Ход игрока Player 1 (ставит Х)")
            move = input_processing(positions)
            field[positions[move][0]][positions[move][1]] =  "X"
            positions.pop(move)
        else:
            print("Ход игрока Player 2 (ставит О)")
            move = input_processing(positions)
            field[positions[move][0]][positions[move][1]] =  "O"
            positions.pop(move)

        examination = victory_check(field, vin_position)
        if examination!=-1:
            os.system('cls' if os.name == 'nt' else 'clear')
            conclusion(field)
            print(f"Победил Player {examination}")
            break
        elif len(positions)==0:
            os.system('cls' if os.name == 'nt' else 'clear')
            conclusion(field)
            print("Ничья")
            break
        whose_move = not whose_move

mode_PvP()




