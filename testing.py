class Character:
    def __init__(self, char_name, char_class):
        self.char_name = char_name
        self.char_class = char_class

    def attack(char_name, char_class):
        """Docstraing."""
        if char_class == 'warrior':
            return f'{self.char_name} нанёс урон противнику равный {5 + randint(3, 5)}'
        if char_class == 'mage':
            return f'{self.char_name} нанёс урон противнику равный {5 + randint(5, 10)}'
        if char_class == 'healer':
            return f'{self.char_name} нанёс урон противнику равный {5 + randint(-3, -1)}'

    def defence(char_name, char_class):
        """Docstraing."""
        if char_class == 'warrior':
            return f'{self.char_name} блокировал {10 + randint(5, 10)} урона'
        if char_class == 'mage':
            return f'{self.char_name} блокировал {10 + randint(-2, 2)} урона'
        if char_class == 'healer':
            return f'{self.char_name} блокировал {10 + randint(2, 5)} урона'

    def special(char_name, char_class):
        """Docstraing."""
        if char_class == 'warrior':
            return f'{self.char_name} применил специальное умение «Выносливость {80 + 25}»'
        if char_class == 'mage':
            return f'{self.char_name} применил специальное умение «Атака {5 + 40}»'
        if char_class == 'healer':
            return f'{self.char_name} применил специальное умение «Защита {10 + 30}»