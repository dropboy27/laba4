from classes.GooseClass import Goose


class GooseCollection():
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
        if not isinstance(item, Goose):
            raise TypeError("Можно добавлять только объекты Goose")
        if item in self._data:
            print(f"[GOOSE_COLLECTION] Гусь {item.name} уже в коллекции")
            return False

        self._data.append(item)
        print(f"[GOOSE_COLLECTION] Гусь {item.name} добавлен")
        return True

    def remove(self, item):
        if item not in self._data:
            print(f"[GOOSE_COLLECTION] Гусь {item.name} не найден")
            return False
        self._data.remove(item)
        print(f"[GOOSE_COLLECTION] Гусь {item.name} удален")
        return True

    def remove_by_name(self, name):
        for goose in self._data:
            if goose.name == name:
                self._data.remove(goose)
                print(f"[GOOSE_COLLECTION] Гусь {name} удален")
                return None
        print(f"[GOOSE_COLLECTION] Гусь {name} не найден")
        return None

    def pop(self, index=-1):
        if len(self) == 0:
            print("[GOOSE_COLLECTION] Коллекция пуста")
            return None
        try:
            goose = self._data.pop(index)
            print(
                f"[GOOSE_COLLECTION] Гусь {goose.name} удален (индекс {index})")
            return goose
        except IndexError:
            print(f"[GOOSE_COLLECTION] Индекс {index} вне диапазона")
            return None
