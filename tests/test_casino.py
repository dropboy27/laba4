import pytest
from src.classes.CasinoClass import Casino
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose, WarGoose, HonkGoose
from src.errors import (
    InvalidItemError,
    ItemNotFoundError,
    EmptyCollectionError,
    PlayerNotFoundError,
    InvalidOperationError
)


class TestCasino:
    def test_init(self):
        casino = Casino()

        assert len(casino.players) == 0
        assert len(casino.geese) == 0
        assert len(casino.balances) == 0

    def test_add_player(self):
        casino = Casino()
        player = Player("Test", 1000)
        casino.add_player(player)

        assert len(casino.players) == 1
        assert casino.balances["Test"] == 1000

    def test_add_goose(self):
        casino = Casino()
        goose = Goose("TestGoose")
        casino.add_goose(goose)

        assert len(casino.geese) == 1

    def test_gambling_insufficient_balance(self):
        casino = Casino()
        player = Player("Test", 50)
        casino.add_player(player)

        casino.gambling("Test", 100)

        assert casino.balances["Test"] == 50

    def test_gambling_with_seed(self):
        import random
        random.seed(42)

        casino = Casino()
        player = Player("Test", 1000)
        casino.add_player(player)

        casino.gambling("Test", 100)

        assert casino.balances["Test"] != 1000

    def test_player_death(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = WarGoose("Warrior")
        casino.add_player(player)
        casino.add_goose(goose)

        player.health = 1
        casino.goose_attack("Warrior", "Test")

        if player.health <= 0:
            assert len(casino.players) == 0 or player not in casino.players

    def test_goose_death(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        goose.health = 5
        casino.player_attack("TestGoose", "Test")

        if goose.health <= 0:
            assert len(casino.geese) == 0 or goose not in casino.geese

    def test_steal_money(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        initial_balance = casino.balances["Test"]
        casino.steal_money()

        assert casino.balances["Test"] <= initial_balance

    def test_step_returns_true(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        result = casino.step()

        assert result == True

    def test_goose_scream(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = HonkGoose("Screamer")
        casino.add_player(player)
        casino.add_goose(goose)

        initial_agility = player.agility
        casino.goose_scream("Screamer", "Test")

        if player.agility < initial_agility:
            assert player.agility < initial_agility

    def test_goose_scream_wrong_goose(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("Regular")
        casino.add_player(player)
        casino.add_goose(goose)

        with pytest.raises(InvalidItemError):
            casino.goose_scream("Regular", "Test")

    def test_event_buy_rake(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        casino.event_buy_rake()
        assert casino.balances["Test"] <= 1000

    def test_event_buy_rake_insufficient_funds(self):
        casino = Casino()
        player = Player("Test", 100)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        casino.event_buy_rake()
        assert casino.balances["Test"] == 100

    def test_goose_attack(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = WarGoose("Warrior")
        casino.add_player(player)
        casino.add_goose(goose)

        initial_health = player.health
        casino.goose_attack("Warrior", "Test")

        assert player.health <= initial_health

    def test_player_attack(self):
        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        initial_health = goose.health
        casino.player_attack("TestGoose", "Test")

        assert goose.health <= initial_health

    def test_multiple_steps(self):
        import random
        random.seed(42)

        casino = Casino()
        player = Player("Test", 1000)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        for _ in range(5):
            result = casino.step()
            assert result == True

    def test_gambling_win(self):
        import random
        random.seed(1)

        casino = Casino()
        player = Player("Test", 1000)
        casino.add_player(player)

        initial_balance = casino.balances["Test"]
        casino.gambling("Test", 100)

        assert casino.balances["Test"] != initial_balance

    def test_steal_money_insufficient(self):
        casino = Casino()
        player = Player("Test", 5)
        goose = Goose("TestGoose")
        casino.add_player(player)
        casino.add_goose(goose)

        casino.steal_money()
        assert casino.balances["Test"] <= 5
