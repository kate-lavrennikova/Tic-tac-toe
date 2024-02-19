import pytest
from tic_tac_toe.game_state import GameState



def test_cell_is_empty(initial_game_state, game_in_progress_state):
    assert initial_game_state.cell_is_empty(1, 1) == True
    assert game_in_progress_state.cell_is_empty(1, 1) == False


