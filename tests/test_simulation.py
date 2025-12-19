import pytest
from src.run_simulation_function import run_simulation
from src.classes.CasinoClass import Casino
from src.classes.PlayerClass import Player
from src.classes.GooseClass import Goose


def test_simulation_runs():
    try:
        run_simulation(steps=5, seed=42)
        assert True
    except Exception:
        assert False


def test_simulation_with_seed_reproducible():
    import random
    from io import StringIO
    import sys

    old_stdout = sys.stdout

    sys.stdout = StringIO()
    run_simulation(steps=3, seed=100)
    output1 = sys.stdout.getvalue()

    sys.stdout = StringIO()
    run_simulation(steps=3, seed=100)
    output2 = sys.stdout.getvalue()

    sys.stdout = old_stdout

    assert output1 == output2


def test_empty_simulation():
    casino = Casino()
    result = casino.step()

    assert result == None
