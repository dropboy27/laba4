from src.classes.CasinoClass import Casino
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose, WarGoose, HonkGoose
from src.run_simulation_function import run_simulation


def main() -> None:
    run_simulation(steps=20, seed=42)


if __name__ == "__main__":
    main()
