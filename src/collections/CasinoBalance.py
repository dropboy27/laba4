class CasinoBalance:
    def __init__(self):
        self._data = {}

    def __setitem__(self, key, value):
        if key in self._data:
            old_balance = self._data[key]
            self._data[key] = value
            print(f"[CASINO] Баланс {key}: {old_balance} -> {value}")
        else:
            self._data[key] = value
            print(f"[CASINO] Новый игрок {key} с балансом {value}")

    def __getitem__(self, key):
        if key in self._data:
            return self._data[key]
        else:
            raise KeyError

    def __len__(self):
        return len(self._data)

    def __delitem__(self, key):
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError

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
            raise ValueError

    def subtract_balance(self, player, amount):
        if amount > 0:
            if player in self._data:
                balance = self[player]
            else:
                balance = 0
            new_balance = balance-amount
            self[player] = new_balance
            print(
                f"[CASINO] Баланс {player}: {balance} - {amount} -> {new_balance}")
        else:
            raise ValueError
