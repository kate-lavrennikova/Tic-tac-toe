from tic_tac_toe.game_state import GameState
import pytest

@pytest.fixture(scope="class")
def initial_game_state():
    return GameState()

@pytest.fixture(scope="class")
def game_in_progress_state():
    return GameState(
        target_x=0,
        target_y=0,
        is_user_move=True,
        moves=[
            [None, "o", None],
            [None, "x", None],
            [None, None, "x"]
        ],
        end_of_game=False,
        win=False,
        filled_cells_count=3,
        is_x = False
    )