import pytest
from src.classes.ChipClass import Chip
from src.game_collections.Chip import ChipCollection
from src.game_collections.Player import PlayerCollection
from src.game_collections.Goose import GooseCollection
from src.game_collections.CasinoBalance import CasinoBalance
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose
from src.errors import (
    InvalidItemError,
    ItemNotFoundError,
    EmptyCollectionError,
    PlayerNotFoundError,
    InvalidOperationError,
    NotEnoughMoneyError
)


class TestPlayerCollection:
    def test_append_player(self):
        collection = PlayerCollection()
        player = Player("Test", 100)
        result = collection.append(player)

        assert result == True
        assert len(collection) == 1
        assert collection[0] == player

    def test_append_duplicate(self):
        collection = PlayerCollection()
        player = Player("Test", 100)
        collection.append(player)
        result = collection.append(player)

        assert result == False
        assert len(collection) == 1

    def test_remove_player(self):
        collection = PlayerCollection()
        player = Player("Test", 100)
        collection.append(player)
        result = collection.remove(player)

        assert result == True
        assert len(collection) == 0

    def test_remove_nonexistent(self):
        collection = PlayerCollection()
        player = Player("Test", 100)

        with pytest.raises(ItemNotFoundError):
            collection.remove(player)

    def test_getitem_index(self):
        collection = PlayerCollection()
        player1 = Player("Test1", 100)
        player2 = Player("Test2", 200)
        collection.append(player1)
        collection.append(player2)

        assert collection[0] == player1
        assert collection[1] == player2

    def test_getitem_slice(self):
        collection = PlayerCollection()
        player1 = Player("Test1", 100)
        player2 = Player("Test2", 200)
        collection.append(player1)
        collection.append(player2)

        slice_result = collection[0:2]
        assert len(slice_result) == 2

    def test_iter(self):
        collection = PlayerCollection()
        player1 = Player("Test1", 100)
        player2 = Player("Test2", 200)
        collection.append(player1)
        collection.append(player2)

        players = list(collection)
        assert len(players) == 2
        assert players[0] == player1

    def test_pop_last(self):
        collection = PlayerCollection()
        player1 = Player("Test1", 100)
        player2 = Player("Test2", 200)
        collection.append(player1)
        collection.append(player2)

        popped = collection.pop()
        assert popped == player2
        assert len(collection) == 1

    def test_pop_index(self):
        collection = PlayerCollection()
        player1 = Player("Test1", 100)
        player2 = Player("Test2", 200)
        collection.append(player1)
        collection.append(player2)

        popped = collection.pop(0)
        assert popped == player1
        assert len(collection) == 1

    def test_pop_empty(self):
        collection = PlayerCollection()

        with pytest.raises(EmptyCollectionError):
            collection.pop()

    def test_remove_by_name(self):
        collection = PlayerCollection()
        player = Player("Test", 100)
        collection.append(player)

        collection.remove_by_name("Test")
        assert len(collection) == 0

    def test_remove_by_name_nonexistent(self):
        collection = PlayerCollection()

        with pytest.raises(ItemNotFoundError):
            collection.remove_by_name("Nonexistent")

    def test_append_wrong_type(self):
        collection = PlayerCollection()

        with pytest.raises(InvalidItemError):
            collection.append("not a player")

    def test_pop_invalid_index(self):
        collection = PlayerCollection()
        player = Player("Test", 100)
        collection.append(player)

        with pytest.raises(ItemNotFoundError):
            collection.pop(10)


class TestGooseCollection:
    def test_append_goose(self):
        collection = GooseCollection()
        goose = Goose("Test")
        result = collection.append(goose)

        assert result == True
        assert len(collection) == 1

    def test_remove_goose(self):
        collection = GooseCollection()
        goose = Goose("Test")
        collection.append(goose)
        result = collection.remove(goose)

        assert result == True
        assert len(collection) == 0

    def test_pop(self):
        collection = GooseCollection()
        goose = Goose("Test")
        collection.append(goose)

        popped = collection.pop()
        assert popped == goose
        assert len(collection) == 0

    def test_remove_by_name(self):
        collection = GooseCollection()
        goose = Goose("Test")
        collection.append(goose)

        collection.remove_by_name("Test")
        assert len(collection) == 0

    def test_append_wrong_type(self):
        collection = GooseCollection()

        with pytest.raises(InvalidItemError):
            collection.append("not a goose")

    def test_pop_index(self):
        collection = GooseCollection()
        goose1 = Goose("Test1")
        goose2 = Goose("Test2")
        collection.append(goose1)
        collection.append(goose2)

        popped = collection.pop(0)
        assert popped == goose1
        assert len(collection) == 1

    def test_pop_invalid_index(self):
        collection = GooseCollection()
        goose = Goose("Test")
        collection.append(goose)

        with pytest.raises(ItemNotFoundError):
            collection.pop(10)

    def test_remove_by_name_nonexistent(self):
        collection = GooseCollection()

        with pytest.raises(ItemNotFoundError):
            collection.remove_by_name("Nonexistent")


class TestCasinoBalance:
    def test_setitem_new_player(self):
        balance = CasinoBalance()
        balance["Test"] = 1000

        assert balance["Test"] == 1000
        assert len(balance) == 1

    def test_setitem_update_balance(self):
        balance = CasinoBalance()
        balance["Test"] = 1000
        balance["Test"] = 1500

        assert balance["Test"] == 1500

    def test_getitem_nonexistent(self):
        balance = CasinoBalance()

        with pytest.raises(PlayerNotFoundError):
            _ = balance["Nonexistent"]

    def test_contains(self):
        balance = CasinoBalance()
        balance["Test"] = 1000

        assert "Test" in balance
        assert "Other" not in balance

    def test_delitem(self):
        balance = CasinoBalance()
        balance["Test"] = 1000
        del balance["Test"]

        assert "Test" not in balance

    def test_add_balance(self):
        balance = CasinoBalance()
        balance["Test"] = 1000
        balance.add_balance("Test", 500)

        assert balance["Test"] == 1500

    def test_subtract_balance(self):
        balance = CasinoBalance()
        balance["Test"] = 1000
        balance.subtract_balance("Test", 300)

        assert balance["Test"] == 700

    def test_iter(self):
        balance = CasinoBalance()
        balance["Player1"] = 1000
        balance["Player2"] = 2000

        players = list(balance)
        assert len(players) == 2
        assert "Player1" in players

    def test_delitem_nonexistent(self):
        balance = CasinoBalance()

        with pytest.raises(PlayerNotFoundError):
            del balance["Nonexistent"]

    def test_add_balance_negative(self):
        balance = CasinoBalance()
        balance["Test"] = 1000

        with pytest.raises(InvalidOperationError):
            balance.add_balance("Test", -100)

    def test_subtract_balance_negative(self):
        balance = CasinoBalance()
        balance["Test"] = 1000

        with pytest.raises(InvalidOperationError):
            balance.subtract_balance("Test", -100)

    def test_add_balance_new_player(self):
        balance = CasinoBalance()
        balance.add_balance("NewPlayer", 500)

        assert balance["NewPlayer"] == 500

    class TestChipCollection:

        def test_append_chip(self):
            collection = ChipCollection()
            chip = Chip(100, "player1")
            collection.append(chip)

            assert len(collection) == 1
            assert collection[0] == chip

        def test_append_wrong_type(self):
            collection = ChipCollection()

            with pytest.raises(InvalidItemError):
                collection.append("not a chip")

        def test_getitem(self):
            collection = ChipCollection()
            chip = Chip(50, "player1")
            collection.append(chip)

            assert collection[0] == chip

        def test_delitem(self):
            collection = ChipCollection()
            chip = Chip(25, "player1")
            collection.append(chip)

            del collection[0]
            assert len(collection) == 0

        def test_pop_last(self):
            collection = ChipCollection()
            chip1 = Chip(100, "player1")
            chip2 = Chip(50, "player2")
            collection.append(chip1)
            collection.append(chip2)

            popped = collection.pop()
            assert popped == chip2
            assert len(collection) == 1

        def test_pop_index(self):
            collection = ChipCollection()
            chip1 = Chip(100, "player1")
            chip2 = Chip(50, "player2")
            collection.append(chip1)
            collection.append(chip2)

            popped = collection.pop(0)
            assert popped == chip1
            assert len(collection) == 1

        def test_pop_empty(self):
            collection = ChipCollection()

            with pytest.raises(EmptyCollectionError):
                collection.pop()

        def test_pop_invalid_index(self):
            collection = ChipCollection()
            chip = Chip(100, "player1")
            collection.append(chip)

            with pytest.raises(ItemNotFoundError):
                collection.pop(10)

        def test_remove_by_value(self):
            collection = ChipCollection()
            chip = Chip(100, "player1")
            collection.append(chip)

            collection.remove_by_value(100)
            assert len(collection) == 0

        def test_remove_by_value_nonexistent(self):
            collection = ChipCollection()

            with pytest.raises(ItemNotFoundError):
                collection.remove_by_value(999)

        def test_len(self):
            collection = ChipCollection()
            chip1 = Chip(100, "player1")
            chip2 = Chip(50, "player2")
            collection.append(chip1)
            collection.append(chip2)

            assert len(collection) == 2

        def test_iter(self):
            collection = ChipCollection()
            chip1 = Chip(100, "player1")
            chip2 = Chip(50, "player2")
            collection.append(chip1)
            collection.append(chip2)

            chips = list(collection)
            assert len(chips) == 2
            assert chips[0] == chip1
            assert chips[1] == chip2
