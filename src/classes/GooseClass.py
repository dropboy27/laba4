from random import random


class Goose():
    def __init__(self, name, honk_volume=30, health=50, agility=50, max_health=50):
        self.name = name
        self.max_health = max_health
        self.health = health
        self.honk_volume = honk_volume
        self.agility = agility

    def honk(self):
        honk_strength = self.honk_volume * (self.health/self.max_health)
        return honk_strength


class WarGoose(Goose):
    def __init__(self, name, honk_volume=50, health=70, agility=40, max_health=70, attack_power=100):
        super().__init__(name, honk_volume, health, agility, max_health)
        self.attack_power = attack_power

    def attack(self):
        return self.attack_power


class HonkGoose(Goose):
    def __init__(self, name, honk_volume=100, health=30, agility=60, max_health=30):
        super().__init__(name, honk_volume, health, agility, max_health)

    def scream(self):
        '''Если станит, то уменьшает агилити человека на 10'''
        stan_chance = self.health/self.max_health*self.agility*random()
        if stan_chance > 42:
            stan = True
        else:
            stan = False
        return stan
