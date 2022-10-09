# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

from random import randint, randrange

letters = "qwertyuiopasdfghjklzxcvbnm"

def compressed_string(random_string):

    count = 0
    count_val = random_string[0]
    rezult_str = ''
    for val in random_string:
        if count_val==val:
            count+=1
        else:
            rezult_str+=f"{count}{count_val}"
            count=1
            count_val=val
    else:
        rezult_str+=f"{count}{count_val}"
        return rezult_str


def recovered_string(new_string):

    rezult_str = ''
    number = ''
    for val in new_string:
        if val.isdigit():
            number+=val
        else:
            rezult_str+=int(number)*val
            number=''
    return rezult_str


random_string = ''.join([val*randrange(1, 16) for val in letters if randint(0,1)])
print(random_string)

compressed_str = compressed_string(random_string)
print(compressed_str)

recovered_str = recovered_string(compressed_str)
print(recovered_str)

