import pytest
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose, WarGoose, HonkGoose
from src.classes.ChipClass import Chip


class TestPlayer:
    def test_init(self):
        player = Player("Test", 1000)

        assert player.name == "Test"
        assert player.balance == 1000
        assert player.health == 100
        assert player.agility == 50

    def test_check_balance(self):
        player = Player("Test", 1000)

        assert player.check_balance() == 1000

    def test_check_health(self):
        player = Player("Test", 1000)

        assert player.check_health() == 100


class TestGoose:
    def test_init(self):
        goose = Goose("TestGoose")

        assert goose.name == "TestGoose"
        assert goose.health == 50
        assert goose.agility == 50
        assert goose.honk_volume == 30

    def test_honk(self):
        goose = Goose("TestGoose")
        result = goose.honk()

        assert isinstance(result, (int, float))
        assert result > 0


class TestWarGoose:
    def test_init(self):
        goose = WarGoose("Warrior")

        assert goose.name == "Warrior"
        assert hasattr(goose, 'attack_power')
        assert goose.attack_power == 100

    def test_inheritance(self):
        goose = WarGoose("Warrior")

        assert isinstance(goose, Goose)
        result = goose.honk()
        assert isinstance(result, (int, float))


class TestHonkGoose:
    def test_init(self):
        goose = HonkGoose("Screamer")

        assert goose.name == "Screamer"
        assert goose.honk_volume == 100

    def test_scream_success(self):
        goose = HonkGoose("Screamer")
        result = goose.scream()

        assert isinstance(result, bool)

    def test_inheritance(self):
        goose = HonkGoose("Screamer")

        assert isinstance(goose, Goose)


class TestChip:
    def test_init(self):
        chip = Chip(100, "Player1")

        assert chip.value == 100
        assert chip.owner == "Player1"

    def test_add_same_owner(self):
        chip1 = Chip(100, "Player1")
        chip2 = Chip(50, "Player1")
        result = chip1 + chip2

        assert result.value == 150
        assert result.owner == "Player1"

    def test_add_different_owners(self):
        chip1 = Chip(100, "Player1")
        chip2 = Chip(50, "Player2")
        result = chip1 + chip2

        assert result.value == 150
        assert result.owner == "Casino"

    def test_add_with_int(self):
        chip = Chip(100, "Player1")
        result = chip + 50

        assert result.value == 150
        assert result.owner == "Player1"

    def test_split(self):
        chip = Chip(100, "Player1")
        chip1, chip2 = chip.split()

        assert chip1.value == 50
        assert chip2.value == 50
        assert chip1.owner == "Player1"

    def test_split_too_small(self):
        chip = Chip(40, "Player1")

        with pytest.raises(ValueError):
            chip.split()
