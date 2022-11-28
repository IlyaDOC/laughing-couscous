from random import randrange

#---------------------------------------ВВОД ЧИСЛА------------------------------------------------
def check_number():
    while True:
        result = input('Введите число: ')
        if result.isdigit() == False:
            print('А может быть все-таки введем целое число?')
            True
        else:
            return int(result)



#------------------------------------------ВЫБОР УРОВНЯ СЛОЖНОСТИ---------------------------------------------
def choosing_lvl():
     print('Выберете уровень сложности (введите цифру от 1 до 4): ', '1) Легкий. Диапазон от 0 до 100', '2) Средний. Диапазон от 0 до 1000', '3) Сложный. Диапазон от 0 до 10000', '4) Безумие. Диапазон от 0 до 100000', sep='\n', end='\n')
     while True:
        lvl = input()
        if lvl == '1':
            game_range = randrange(1, 101)
            print(f'Вы выбрали легкий уровень сложности')
            return game_range
            break
        elif lvl == '2':
            game_range = randrange(1, 1001)
            print(f'Вы выбрали средний уровень сложности')
            return game_range
            break
        elif lvl == '3':
            game_range = randrange(1, 10001)
            print(f'Вы выбрали сложный уровень сложности')
            return game_range
            break
        elif lvl == '4':
            game_range = randrange(1, 100001)
            print(f'Вы выбрали безумный уровень сложности')
            return game_range
            break
        else:
            print('Вы допустили ошибку, попробуйте еще раз!')
            True

#------------------------------------НАЧАЛО ИГРЫ---------------------------------------------
def start_game():

        while True:
            start = input()
            if start=='y':
                print('Погнали!')
                return True
                False
            elif start=='n':
                print('Жаль! До встречи!')
                return False
                False
            else:
                print('Вы ввели некорректный ответ')
                True

#---------------------------------------ОСНОВНАЯ ЧАСТЬ--------------------------------------------
def main_part():
    count = 0
    num = choosing_lvl()
    while True:
        my_number = check_number()
        if my_number>num:
            count+=1
            print('Слишком много, попробуйте еще раз')
            True
        elif my_number<num:
            count+=1
            print('Слишком мало, попробуйте еще раз')
            True
        else:
            count+=1
            print(f'Вы угадали с {count} попытки, поздравляем!')
            False
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

#------------------------------------ПОВТОРИТЬ ИГРУ---------------------------------------
def continue_game():
    print('Хотите повторить игру? да=y/нет=n\n')
    while True:
        answer = input()
        if answer == 'y':
            return True
        elif answer =='n':
            return False
        else:
            print('Повторите попытку!')


#------------------------------------ТЕЛО ИГРЫ---------------------------------------------
def game():
    print('Добро пожаловать в числовую угадайку', 'Вы хотиете сыграть в игру? да=y/нет=n')
    while True:
        if start_game()==False:
            False
            break
        else:
            True
        if main_part()==True:
            True
        else:
            if continue_game() == True:
                True
            else:
                break


game()
