from src.classes.PlayerClass import Player


class PlayerCollection():
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        if isinstance(index, (int | slice)):
            return self._data[index]
        else:
            raise TypeError("Индекс должен быть int или slice")

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def append(self, item):
        if not isinstance(item, Player):
            raise TypeError("Можно добавлять только объекты Player")
        if item in self._data:
            print(f"[PLAYER_COLLECTION] Игрок {item.name} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[PLAYER_COLLECTION] Игрок {item.name} добавлен")
        return True

    def remove(self, item):
        if item not in self._data:
            print(f"[PLAYER_COLLECTION] Игрок {item.name} не найден")
            return False
        self._data.remove(item)
        print(f"[PLAYER_COLLECTION] Игрок {item.name} удален")
        return True

    def remove_by_name(self, name):
        for player in self._data:
            if player.name == name:
                self._data.remove(player)
                print(f"[PLAYER_COLLECTION] Игрок {name} удален")
                return None
        print(f"[PLAYER_COLLECTION] Игрок {name} не найден")
        return None

    def pop(self, index=-1):
        if len(self) == 0:
            print("[PLAYER_COLLECTION] Коллекция пуста")
            return None
        try:
            player = self._data.pop(index)
            print(
                f"[PLAYER_COLLECTION] Игрок {player.name} удален (индекс {index})")
            return player
        except IndexError:
            print(f"[PLAYER_COLLECTION] Индекс {index} вне диапазона")
            return None
