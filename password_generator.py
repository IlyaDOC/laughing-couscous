import string
from random import choice
#------------------------------СПИСКИ СИМВОЛОВ--------------------------------------
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
punctuation = list(string.punctuation)
ambiguous_characters = list('il1Lo0O')

#---------------------------ВКЛЮЧЕНИЕ СИМВОЛОВ-------------------------------------
def char_list():
    # ---------------------------------ВЫБОР ВКЛЮЧЕНИЯ СИМВОЛОВ----------------------------
    print('Выберите какие символы стоит включать в пароль')
    add_digits = input('Включать цифры? да=y/нет=n\n')
    add_uppercase = input('Включать прописные буквы? да=y/нет=n\n')
    add_lowercase = input('Включать строчные буквы? да=y/нет=n\n')
    add_punctuation = input('Включать знаки пунктуации? да=y/нет=n\n')
    add_ambiguous = input('Включать ли неоднозначные символы? да=y/нет=n\n')
    chars = [] #ПЕРЕМЕННАЯ ДЛЯ ВКЛЮЧЕНИЯ ПАРОЛЕЙ
    if add_digits == 'y':
        chars.extend(digits)
    if add_uppercase =='y':
        chars.extend(uppercase_letters)
    if add_lowercase == 'y':
        chars.extend(lowercase_letters)
    if add_punctuation == 'y':
        chars.extend(punctuation)
    if add_ambiguous == 'y':
        chars.extend(ambiguous_characters)
    return chars
# ---------------------------------ВЫБОР КОЛИЧЕСТВА ПАРОЛЕЙ-----------------------------
def amount_of_passwords():
    number_of_passwords = int(input('Введите количество паролей, которое нужно сгенерировать: '))
    return number_of_passwords
#--------------------------------ВЫБОР ДЛИННЫ ПАРОЛЯ-------------------------------------
def len_pass():
    length_of_password = int(input('Введите длинну пароля: '))
    return length_of_password

def password_generator():
    print('Добро пожаловать! Это генератор паролей!')
    my_list = char_list()
    length = len_pass()
    n = amount_of_passwords()

    for i in range(n):
        password = ''
        for j in range(length):
            password += choice(my_list)
        print(password, sep='\n')
    print()
password_generator()
