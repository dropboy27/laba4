from classes.ChipClass import Chip


class ChipCollection():
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
        if not isinstance(item, Chip):
            raise TypeError("Можно добавлять только объекты Chip")
        if item in self._data:
            print(f"[CHIP_COLLECTION] Фишка {item.name} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[CHIP_COLLECTION] Фишка {item.name} добавлена")
        return True

    def remove(self, item):
        if item not in self._data:
            print(f"[CHIP_COLLECTION] Фишка {item.name} не найдена")
            return False
        self._data.remove(item)
        print(f"[CHIP_COLLECTION] Фишка {item.name} удалена")
        return True

    def remove_by_name(self, name):
        for player in self._data:
            if player.name == name:
                self._data.remove(player)
                print(f"[CHIP_COLLECTION] Фишка {name} удалена")
                return None
        print(f"[CHIP_COLLECTION] Фишка {name} не найдена")
        return None

    def pop(self, index=-1):
        if len(self) == 0:
            print("[CHIP_COLLECTION] Коллекция пуста")
            return None
        try:
            player = self._data.pop(index)
            print(
                f"[CHIP_COLLECTION] Фишка {player.name} удалена (индекс {index})")
            return player
        except IndexError:
            print(f"[CHIP_COLLECTION] Индекс {index} вне диапазона")
            return None
