from src.classes.ChipClass import Chip


class ChipCollection():
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        if isinstance(index, (int | slice)):
            return self._data[index]
        else:
            raise TypeError("Индекс должен быть int или slice")

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def append(self, item):
        if not isinstance(item, Chip):
            raise TypeError("Можно добавлять только объекты Chip")
        if item in self._data:
            print(f"[CHIP_COLLECTION] Фишка {item.value} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[CHIP_COLLECTION] Фишка {item.value} добавлена")
        return True

    def remove(self, item):
        if item not in self._data:
            print(f"[CHIP_COLLECTION] Фишка {item.value} не найдена")
            return False
        self._data.remove(item)
        print(f"[CHIP_COLLECTION] Фишка {item.value} удалена")
        return True

    def remove_by_value(self, value):
        for chip in self._data:
            if chip.value == value:
                self._data.remove(chip)
                print(f"[CHIP_COLLECTION] Фишка {value} удалена")
                return
        print(f"[CHIP_COLLECTION] Фишка {value} не найдена")
        return None

    def pop(self, index=-1):
        if len(self) == 0:
            print("[CHIP_COLLECTION] Коллекция пуста")
            return None
        try:
            chip = self._data.pop(index)
            print(
                f"[CHIP_COLLECTION] Фишка {chip.value} удалена (индекс {index})")
            return chip
        except IndexError:
            print(f"[CHIP_COLLECTION] Индекс {index} вне диапазона")
            return None
