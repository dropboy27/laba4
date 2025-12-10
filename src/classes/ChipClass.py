class Chip():
    def __init__(self, value, owner):
        self.value = value
        self.owner = owner

    def __add__(self, other):
        if isinstance(other, Chip):
            if other.owner == self.owner:
                new_chip = Chip(self.value + other.value, self.owner)
            else:
                new_chip = Chip(self.value + other.value, "Casino")
        elif isinstance(other, int):
            new_chip = Chip(self.value + other, self.owner)
        else:
            return NotImplemented
        return new_chip

    def split(self):
        if self.value >= 50:
            half = self.value // 2
            chip1 = Chip(half, self.owner)
            chip2 = Chip(half, self.owner)
            return chip1, chip2
        else:
            raise ValueError(
                f"Cannot split chip with value {self.value} (minimum 50)")
