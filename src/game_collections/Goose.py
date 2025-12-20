from src.classes.GooseClass import Goose
from src.errors import InvalidItemError, ItemNotFoundError, EmptyCollectionError


class GooseCollection():
    def __init__(self):
        self._data = []

    def __getitem__(self, index):
        if isinstance(index, (int | slice)):
            return self._data[index]
        else:
            raise InvalidItemError("Индекс должен быть int или slice")

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def append(self, item):
        if not isinstance(item, Goose):
            raise InvalidItemError("Можно добавлять только объекты Goose")
        if item in self._data:
            print(f"[GOOSE_COLLECTION] Гусь {item.name} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[GOOSE_COLLECTION] Гусь {item.name} добавлен")
        return True

    def remove(self, item):
        if item not in self._data:
            raise ItemNotFoundError(f"Гусь {item.name} не найден")
        self._data.remove(item)
        print(f"[GOOSE_COLLECTION] Гусь {item.name} удален")
        return True

    def remove_by_name(self, name):
        for goose in self._data:
            if goose.name == name:
                self._data.remove(goose)
                print(f"[GOOSE_COLLECTION] Гусь {name} удален")
                return None
        raise ItemNotFoundError(f"Гусь с именем {name} не найден")

    def pop(self, index=-1):
        if len(self) == 0:
            raise EmptyCollectionError("Коллекция гусей пуста")
        try:
            goose = self._data.pop(index)
            print(
                f"[GOOSE_COLLECTION] Гусь {goose.name} удален (индекс {index})")
            return goose
        except IndexError:
            raise ItemNotFoundError(f"Индекс {index} вне диапазона")
