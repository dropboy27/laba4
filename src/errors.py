class NotEnoughMoneyError(Exception):
    """Недостаточно денег на балансе"""
    pass


class InvalidOperationError(Exception):
    """Некорректная операция с балансом"""
    pass


class PlayerNotFoundError(Exception):
    """Игрок не найден в казино"""
    pass


class InvalidItemError(Exception):
    """Неправильный тип элемента для коллекции"""
    pass


class ItemNotFoundError(Exception):
    """Элемент не найден в коллекции"""
    pass


class EmptyCollectionError(Exception):
    """Операция с пустой коллекцией"""
    pass


class ChipSplitError(Exception):
    """Невозможно разделить фишку"""
    pass


class InvalidStatsError(Exception):
    """Некорректные характеристики существа"""
    pass
