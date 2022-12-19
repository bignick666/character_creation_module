from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name, char_class):
    """Docstraing."""
    if char_class == 'warrior':
        return f'{char_name} нанёс урон противнику равный {5 + randint(3, 5)}'
    if char_class == 'mage':
        return f'{char_name} нанёс урон противнику равный {5 + randint(5, 10)}'
    if char_class == 'healer':
        return f'{char_name} нанёс урон противнику равный {5 + randint(-3, -1)}'


def defence(char_name, char_class):
    """Docstraing."""
    if char_class == 'warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} урона'
    if char_class == 'mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} урона213123123213'
    if char_class == 'healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} урона'


def special(char_name, char_class):
    """Docstraing."""
    if char_class == 'warrior': 
        return f'{char_name} применил специальное умение «Выносливость {80 + 25}»'
    if char_class == 'mage':
        return f'{char_name} применил специальное умение «Атака {5 + 40}»'
    if char_class == 'healer':
        return f'{char_name} применил специальное умение «Защита {10 + 30}»'


def start_training(char_name, char_class):
    """Docstraing."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    """Docstraing."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого хочешь играть:'
                           ' Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, чтобы выбрать другого персонажа ').lower()
        return f'После {len(duel_res)} поединков,' \
               f' репутация персонажа — {current_rep:.3f} очков.'


def main() -> None:
    """Docstraing."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()

<<<<<<< HEAD


# Тестовые данные.
TEST_DATA: list = [
    (44, 'success', True),
    (16, 'failure', True),
    (4, 'success', False),
    (21, 'failure', False),
]

BONUS: float = 1.1
ANTIBONUS: float = 0.8


def add_rep(current_rep: float, rep_points: float, buf_effect: float) -> float:
    current_rep += rep_points
    if buf_effect:
        return current_rep * BONUS
    return current_rep


def remove_rep(current_rep: float, rep_points: float, debuf_effect: float):
    current_rep -= rep_points
    if debuf_effect:
        return current_rep * ANTIBONUS
    return current_rep


def main(duel_res: list) -> str:
    current_rep = 0.0
    for rep, result, effect in duel_res:
        if result == 'success':
            current_rep = add_rep(current_rep, rep, effect)
        if result == 'failure':
            current_rep = remove_rep(current_rep, rep, effect)
    return f'После {len(duel_res)} поединков,' \
           f' репутация персонажа — {current_rep:.3f} очков.'


# Тестовый вызов функции main.
print(main(TEST_DATA))
=======
if __name__ == '__main__':
    """Docstraing."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))
>>>>>>> 868fbfd379e161046f700667d58ce4acb7e96ea5
