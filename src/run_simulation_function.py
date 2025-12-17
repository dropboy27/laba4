import random
from src.classes.CasinoClass import Casino
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose, WarGoose, HonkGoose


def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    casino = Casino()

    casino.add_player(Player("Хорус Луперкаль", 1000))
    casino.add_player(Player("Фулгрим", 1500))
    casino.add_player(Player("Мортарион", 800))

    casino.add_goose(WarGoose("Леман Русс"))
    casino.add_goose(HonkGoose("Сангвиний"))
    casino.add_goose(Goose("Робаут Жиллиман"))

    print(f"=== Симуляция казино на {steps} шагов ===\n")

    for i in range(steps):
        print(f"\n--- Шаг {i+1} ---")
        casino.step()

    print("\n=== Симуляция завершена ===")
    print("\nФинальные результаты:")
    for player in casino.players:
        print(
            f"{player.name}: баланс={casino.balances[player.name]}, HP={player.health}")
    for goose in casino.geese:
        print(
            f"{goose.name}: , HP={player.health}")

    alive_players = [p for p in casino.players if p.health > 0]
    alive_geese = [g for g in casino.geese if g.health > 0]

    print(f"\nЖивых игроков: {len(alive_players)}")
    print(f"Живых гусей: {len(alive_geese)}")

    if len(alive_players) > len(alive_geese):
        print("\nПОБЕДА ЛЮДЕЙ")
    elif len(alive_geese) > len(alive_players):
        print("\nПОБЕДА ГУСЕЙ!")
    else:
        print("\nНИЧЬЯ!")
