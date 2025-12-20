from src.errors import InvalidStatsError


class Player():
    def __init__(self, name, balance, health=100, agility=50):
        if health < 0 or agility < 0:
            raise InvalidStatsError(
                "Здоровье и ловкость не могут быть отрицательными")
        if balance < 0:
            raise InvalidStatsError(
                "Начальный баланс не может быть отрицательным")

        self.name = name
        self.balance = balance
        self.health = health
        self.agility = agility

    def check_balance(self):
        return self.balance

    def check_health(self):
        return self.health
