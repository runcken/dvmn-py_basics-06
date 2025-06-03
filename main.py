def is_very_long(password):
    return int(len(password) > 11)


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_symbols(password):
    return any(not char.isalnum() for char in password)


def main():
    password = input('Введите пароль: ')
    score = 0
    functions = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols
    ]
    for func in functions:
        score += func(password)
    print('Рейтинг пароля:', score*2)


if __name__ == '__main__':
    main()
