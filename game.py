# -*- coding: utf-8 -*-
from random import randint, choice
from time import sleep


class Player:
    """ Класс игрока. Принимающий имя игрока и имеюющий флаг PC,
    который определяет игрок это или компьютер.
    """

    def __init__(self, name, pc=False):
        self.name = name
        self.health = 100
        self.pc = pc

    def attack(self, target):
        """ Метод отвечающий за обычную атаку,случайным образом выбирает количество урона
        между 18 и 25
        """
        attack_power = randint(18, 25)
        target.health -= attack_power
        print(f"{self.name} атакует {target.name} нанося ему {attack_power} единиц(ы) урона")

        if target.health > 0:
            print(f"Уровень здоровья {target.name} - {target.health}%")
            print('==============')
            print()
        else:
            print(f"Топор {self.name} настиг {target.name}. Земля ему пухом!")
        sleep(1)

    def strong_attack(self, target):
        """ Метод отвечающий за большой урон, выбирает случайное значение между 10-35
        """
        attack_power = randint(10, 35)
        target.health -= attack_power
        print(f"{self.name} яростно атакует {target.name}, нанося ему {attack_power} единиц(ы) урона")

        if target.health > 0:
            print(f"Уровень здоровья {target.name} - {target.health}%")
            print('==============')
            print()
        else:
            print(f"{target.name} был молод и красив, пока не встретился с {self.name}")
        sleep(1)

    def heal(self):
        """ Метод отвечающий за лечение,выбирает случайное кол-во жизней между 18-25.
        При количестве жизней выше 100, устанавлиет значение их на 100.
        """
        heal_amount = randint(18, 25)
        self.health += heal_amount
        if self.health > 100:
            self.health = 100
        print(f"{self.name} исцеляет себя на {heal_amount} единиц(ы)")
        print(f"Уровень здоровья {self.name} - {self.health}%")

        print('==============')
        print()
        sleep(1)


def main():
    """ Функция отвечающая за событие игры.Случайным образом выбирается игрок
    который ходит и так же случайно выбирается навык который он использует.
    """
    hero = Player('Paladin')
    pc = Player('Garosh Hellscream', pc=True)

    while True:
        coin = randint(0, 1)
        if hero.health > 0 and pc.health > 0:
            if coin == 1:
                action = choice([hero.attack, hero.strong_attack, hero.heal])
                if action == hero.heal:
                    hero.heal()
                else:
                    action(pc)
            else:
                if pc.health <= 35:  # Если значение жизней меньше 35,увеличивает шанс лечения.
                    action = choice([pc.attack, pc.strong_attack, pc.heal, pc.heal])
                    if action == pc.heal:
                        pc.heal()
                    else:
                        action(hero)
                else:
                    action = choice([pc.attack, pc.strong_attack, pc.heal])
                    if action == pc.heal:
                        pc.heal()
                    else:
                        action(hero)
        elif pc.health <= 0:
            print(f'{pc.name} повержен, а {hero.name} заслужил отдых.')
            break
        else:
            print(f'{hero.name} доблестно сражался, но погиб. О нем не забудут.')
            break


if __name__ == "__main__":
    main()