from src.errors import NotEnoughMoneyError, PlayerNotFoundError, InvalidOperationError


class CasinoBalance:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        if key in self._data:
            self._data[key] = value
        else:
            self._data[key] = value
            print(f"[CASINO] Новый игрок {key} с балансом {value}")

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            raise PlayerNotFoundError(f"Игрок {key} не найден")

    def __len__(self):
        return len(self._data)

    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]
        else:
            raise PlayerNotFoundError(f"Игрок {key} не найден")

    def __contains__(self, key):
        return key in self._data

    def __iter__(self):
        return iter(self._data)

    def add_balance(self, player, amount):
        if amount >= 0:
            if player in self._data:
                balance = self[player]
            else:
                balance = 0
            new_balance = balance+amount
            self[player] = new_balance
            print(
                f"[CASINO] Баланс {player}: {balance} + {amount} -> {new_balance}")
        else:
            raise InvalidOperationError("Нельзя добавить отрицательную сумму")

    def subtract_balance(self, player, amount):
        if amount <= 0:
            raise InvalidOperationError(
                "Нельзя вычесть отрицательную или нулевую сумму")

        if player in self._data:
            balance = self[player]
        else:
            balance = 0

        if balance < amount:
            raise NotEnoughMoneyError(
                f"У {player} недостаточно денег: {balance} < {amount}")

        new_balance = balance - amount
        self[player] = new_balance
        print(
            f"[CASINO] Баланс {player}: {balance} - {amount} -> {new_balance}")
