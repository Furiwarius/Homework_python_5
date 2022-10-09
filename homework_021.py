# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

bad_word = 'абв'
words = "приабвет здрабвствуйте добрый день приветствую hi hello добро пожаловабвть"
print(words)

list_words = words.split()
corrected_words = " ".join([val for val in list_words if bad_word not in val])
print(corrected_words)