import random as r # Подключите библиотеку random и дайте ей краткое имя

answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    return r.choice(answers)# Напишите ваш код здесь


print(how_are_you())