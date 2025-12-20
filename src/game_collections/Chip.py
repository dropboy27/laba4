from src.classes.ChipClass import Chip
from src.errors import InvalidItemError, ItemNotFoundError, EmptyCollectionError


class ChipCollection():
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        if isinstance(index, (int | slice)):
            return self._data[index]
        else:
            raise InvalidItemError("Индекс должен быть int или slice")

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def append(self, item):
        if not isinstance(item, Chip):
            raise InvalidItemError("Можно добавлять только объекты Chip")
        if item in self._data:
            print(f"[CHIP_COLLECTION] Фишка {item.value} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[CHIP_COLLECTION] Фишка {item.value} добавлена")
        return True

    def remove(self, item):
        if item not in self._data:
            raise ItemNotFoundError(f"Фишка {item.value} не найдена")
        self._data.remove(item)
        print(f"[CHIP_COLLECTION] Фишка {item.value} удалена")
        return True

    def remove_by_value(self, value):
        for chip in self._data:
            if chip.value == value:
                self._data.remove(chip)
                print(f"[CHIP_COLLECTION] Фишка {value} удалена")
                return
        raise ItemNotFoundError(f"Фишка со значением {value} не найдена")

    def pop(self, index=-1):
        if len(self) == 0:
            raise EmptyCollectionError("Коллекция фишек пуста")
        try:
            chip = self._data.pop(index)
            print(
                f"[CHIP_COLLECTION] Фишка {chip.value} удалена (индекс {index})")
            return chip
        except IndexError:
            raise ItemNotFoundError(f"Индекс {index} вне диапазона")
