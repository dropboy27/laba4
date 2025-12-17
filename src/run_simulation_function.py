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

    print(f"\n=== Симуляция казино на {steps} шагов ===\n")

    for i in range(steps):
        print(f"\n--- Шаг {i+1} ---")
        if not casino.step():
            print("\nСимуляция прервана досрочно!")
            break

    print("\n=== Симуляция завершена ===")

    print("\nФинальное состояние ИГРОКОВ:")
    for player in casino.players:
        if player.name in casino.balances:
            balance = casino.balances[player.name]
        else:
            balance = 0
        print(f"  {player.name}: баланс={balance}, HP={player.health}")

    print("\nФинальное состояние ГУСЕЙ:")
    for goose in casino.geese:
        print(f"  {goose.name}: HP={goose.health}")

    alive_players = [p for p in casino.players if p.health > 0]
    alive_geese = [g for g in casino.geese if g.health > 0]

    print(f"\nЖивых игроков: {len(alive_players)}")
    print(f"Живых гусей: {len(alive_geese)}")

    if len(alive_players) > len(alive_geese):
        print("\nПОБЕДА ЛЮДЕЙ!")
    elif len(alive_geese) > len(alive_players):
        print("\nПОБЕДА ГУСЕЙ!")
    else:
        print("\nНИЧЬЯ!")
