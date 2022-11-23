from random import randrange
num = randrange(1,101)
flag = True
while flag == True:
    result = int(input('Пожалуйста, введите загаданное число: '))
    if result>num:
        print('Слишком много, попробуйте еще раз')
        continue
    elif result<num:
        print('Слишком мало, попробуйте еще раз')
        continue
    else:
        print('Вы угадали, поздравляем!')
        flag = False
        break
