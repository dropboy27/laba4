from src.game_collections.CasinoBalance import CasinoBalance
from src.game_collections.Chip import ChipCollection
from src.game_collections.Goose import GooseCollection
from src.game_collections.Player import PlayerCollection
from src.classes.GooseClass import Goose, WarGoose, HonkGoose
from src.classes.PlayerClass import Player

from src.errors import NotEnoughMoneyError
import random


class Casino():
    def __init__(self):
        self.players = PlayerCollection()
        self.geese = GooseCollection()
        self.balances = CasinoBalance()

    def add_player(self, player):
        self.players.append(player)
        self.balances[player.name] = player.balance

    def add_goose(self, goose):
        self.geese.append(goose)

    def gambling(self, player_name, amount):

        if self.balances[player_name] < amount:
            print(
                f"[PLAYER] У игрока {player_name} недостаточно денег для ставки {amount}. Баланс: {self.balances[player_name]}")
            return

        self.balances.subtract_balance(player_name, amount)
        print(f"[PLAYER] Игрок {player_name} делает ставку {amount}")

        if random.random() < 0.5:
            multiplier = random.uniform(1.5, 3.0)
            win = int(amount * multiplier)
            self.balances.add_balance(player_name, win)
            print(f"[GAMBLING] игрок {player_name} ВЫИГРАЛ! Получено {win}")
        else:
            print(f"[GAMBLING] игрок {player_name} Проиграл")

    def goose_attack(self, goose_name, player_name):
        goose = None
        for g in self.geese:
            if g.name == goose_name:
                goose = g
                break

        player = None
        for p in self.players:
            if p.name == player_name:
                player = p
                break

        if not goose or not player:
            print("Гусь или игрок не найден")
            return

        roll = random.randint(1, 20)
        attack_roll = roll * (goose.agility / player.agility)+0.5

        if attack_roll > 10:
            if hasattr(goose, 'attack_power'):
                damage = goose.attack_power
            else:
                damage = goose.honk_volume//4

            player.health -= damage
            print(
                f"[GOOSE] {goose_name} атакует {player_name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПОПАЛ! Урон: {damage}, HP: {player.health}")
            if player.health <= 0:
                print(
                    f"[DEATH] {player_name} пал смертью храбрых от клюва {goose_name}...")
                self.players.remove(player)
                if player.name in self.balances:
                    del self.balances[player.name]
        else:
            print(
                f"[GOOSE] {goose_name} атакует {player_name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПРОМАХ!")

    def goose_scream(self, goose_name, player_name):
        goose = None
        for g in self.geese:
            if g.name == goose_name:
                goose = g
                break

        player = None
        for p in self.players:
            if p.name == player_name:
                player = p
                break

        if not goose or not player:
            print("Гусь или игрок не найден")
            return

        if not isinstance(goose, HonkGoose):
            print("Этот гусь не умеет кричать.")
            return

        stunned = goose.scream()

        if stunned:
            player.agility -= 10
            print(
                f"[GOOSE] {goose_name} КРИЧИТ на {player_name}! Agility уменьшена до {player.agility}")
        else:
            print(
                f"[GOOSE] {goose_name} пытается крикнуть на {player_name}, но не получается")

    def player_attack(self, goose_name, player_name):
        goose = None
        for g in self.geese:
            if g.name == goose_name:
                goose = g
                break

        player = None
        for p in self.players:
            if p.name == player_name:
                player = p
                break

        if not goose or not player:
            print("Гусь или игрок не найден")
            return

        roll = random.randint(1, 20)
        attack_roll = roll * (player.agility / goose.agility)

        if attack_roll > 10:
            damage = 5*random.randint(1, 8)
            goose.health -= damage
            print(
                f"[PLAYER] {player_name} атакует {goose_name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПОПАЛ! Урон: {damage}, HP гуся: {goose.health}")

            if goose.health <= 0:
                print(f"[DEATH] Гусь {goose_name} был сражен {player_name}!")
                self.geese.remove(goose)
        else:
            print(
                f"[PLAYER] {player_name} атакует {goose_name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПРОМАХ!")

    def event_buy_rake(self):
        """Игрок покупает грабли и атакует"""
        player = random.choice(self.players)

        if self.balances[player.name] < 300:
            print(
                f"[GRABLI] {player.name} хочет купить грабли, но нужно 300 (есть {self.balances[player.name]})")
            return

        self.balances.subtract_balance(player.name, 300)
        print(f"[GRABLI] {player.name} купил ГРАБЛИ за 300!")

        if random.random() < 0.5 and len(self.geese) > 0:
            goose = random.choice(self.geese)
            roll = random.randint(1, 20)
            attack_roll = roll * (player.agility / goose.agility)

            if attack_roll > 10:
                damage = 5*random.randint(1, 8) * 2
                goose.health -= damage
                print(
                    f"[GRABLI] {player.name} РАЗМАХИВАЕТ ГРАБЛЯМИ по {goose.name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПОПАЛ! Урон: {damage}, HP гуся: {goose.health}")

                if goose.health <= 0:
                    print(
                        f"[DEATH] Гусь {goose.name} был беспощадно сражен {player.name} при помощи граблей!")
                    self.geese.remove(goose)
            else:
                print(
                    f"[GRABLI] {player.name} замахнулся граблями на {goose.name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПРОМАХ!")

        elif len(self.players) > 1:
            other_players = [p for p in self.players if p.name != player.name]
            if other_players:
                victim = random.choice(other_players)
                roll = random.randint(1, 20)
                attack_roll = roll * (player.agility / victim.agility)

                if attack_roll > 10:
                    stolen = self.balances[victim.name] // 2
                    damage = 5*random.randint(1, 5)
                    victim.health -= damage
                    if stolen > 0:
                        self.balances.subtract_balance(victim.name, stolen)
                        self.balances.add_balance(player.name, stolen)
                        print(
                            f"[GRABLI] {player.name} УДАРИЛ ГРАБЛЯМИ {victim.name} и забрал {stolen} денег и нанес {damage} урона ! Бросок: {roll}, итог: {attack_roll:.2f}")
                    else:
                        print(
                            f"[GRABLI] {player.name} ударил {victim.name} граблями и нанес {damage} урона, но у того нет денег!")
                else:
                    print(
                        f"[GRABLI] {player.name} замахнулся граблями на {victim.name}! Бросок: {roll}, итог: {attack_roll:.2f} - ПРОМАХ!")
        else:
            print(f"[GRABLI] {player.name} купил грабли, но некого атаковать!")

    def steal_money(self):
        """Гусь крадет деньги у игрока"""
        goose = random.choice(self.geese)
        player = random.choice(self.players)

        if self.balances[player.name] < 10:
            print(
                f"[GOOSE] {goose.name} пытается украсть у {player.name}, но денег почти нет")
            return

        stolen = random.randint(10, 1000)
        stolen = min(stolen, self.balances[player.name])

        self.balances.subtract_balance(player.name, stolen)
        print(f"[STEAL] {goose.name} украл {stolen} у {player.name}!")

    def step(self):
        if len(self.players) == 0 or len(self.geese) == 0:
            print("[SIMULATION] Недостаточно участников")
            return

        events = [
            'gambling',
            'goose_attack',
            'goose_scream',
            'player_attack',
            'steal_money',
            'buy_rake'
        ]

        event = random.choice(events)
        if event == 'gambling':
            player = random.choice(self.players)
            amount = random.choice([10, 25, 50, 100]) * random.randint(1, 10)
            self.gambling(player.name, amount)

        elif event == 'goose_attack':
            goose = random.choice(self.geese)
            player = random.choice(self.players)
            self.goose_attack(goose.name, player.name)

        elif event == 'goose_scream':
            honk_geese = [g for g in self.geese if isinstance(g, HonkGoose)]
            if honk_geese:
                goose = random.choice(honk_geese)
                player = random.choice(self.players)
                self.goose_scream(goose.name, player.name)

        elif event == 'player_attack':
            goose = random.choice(self.geese)
            player = random.choice(self.players)
            self.player_attack(goose.name, player.name)
        elif event == 'buy_rake':
            self.event_buy_rake()
        elif event == 'steal_money':
            self.steal_money()
        return True
