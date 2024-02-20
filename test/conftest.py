from tic_tac_toe.game_state import GameState
from tic_tac_toe.game import TicTacToe
import pytest

@pytest.fixture
def initial_game_state():
    return GameState()

@pytest.fixture
def game_state_in_progress():
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

winning_combinations = [
    GameState(
        target_x=0,
        target_y=0,
        is_user_move=True,
        moves=[
            ["x", "o", "o"],
            ["o", "x", None],
            ["o", "x", "x"]
        ],
        end_of_game=False,
        win=False,
        filled_cells_count=8,
        is_x = True
    ),
    GameState(
        target_x=0,
        target_y=2,
        is_user_move=False,
        moves=[
            [None, None, "o"],
            [None, "o", "x"],
            ["o", "x", "x"]
        ],
        end_of_game=False,
        win=False,
        filled_cells_count=6,
        is_x = False
    ),
    GameState(
        target_x=2,
        target_y=1,
        is_user_move=False,
        moves=[
            ["x", "x", "o"],
            ["o", "x", None],
            ["o", "x", None]
        ],
        end_of_game=False,
        win=False,
        filled_cells_count=7,
        is_x = True
    ),
    GameState(
        target_x=0,
        target_y=2,
        is_user_move=True,
        moves=[
            ["o", "o", "o"],
            ["x", None, None],
            ["x", "x", None]
        ],
        end_of_game=False,
        win=False,
        filled_cells_count=6,
        is_x = False
    )
]

ids_of_winning_combinations = ["main_diagonal", "side_diagonal", "column", "row"]


@pytest.fixture(params=winning_combinations, ids=ids_of_winning_combinations)
def game_state_winning_combination(request):
    return request.param

@pytest.fixture
def tic_tac_toe():
    return TicTacToe()
