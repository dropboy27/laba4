class Player():
    def __init__(self, name, balance, health=100, agility=50):
        self.name = name
        self.balance = balance
        self.health = health
        self.agility = agility

    def check_balance(self):
        return self.balance

    def check_health(self):
        return self.health
