import pytest
from tic_tac_toe.game_state import GameState
from contextlib import nullcontext as does_not_raise
from pydantic import ValidationError
from tic_tac_toe.game_state import CellIsFilledException



def test_cell_is_empty(initial_game_state, game_state_in_progress):
    assert initial_game_state.cell_is_empty(1, 1) == True
    assert game_state_in_progress.cell_is_empty(1, 1) == False


def test_check_if_win(game_state_winning_combination):
    game_state_winning_combination.check_if_win()
    assert game_state_winning_combination.end_of_game == True
    assert game_state_winning_combination.win == True

@pytest.mark.parametrize("coordinates, expectation", 
                         [("0 0", does_not_raise()),
                          ("2 1", does_not_raise()),
                          ("00", pytest.raises(IndexError)), 
                          ("asd 0", pytest.raises(ValidationError)), 
                          ("5 4",  pytest.raises(ValidationError)), 
                          ("0 1", pytest.raises(CellIsFilledException))]
                         )
def test_update_coordinates(game_state_in_progress, coordinates, expectation):
    with expectation:
        game_state_in_progress.update_coordinates(coordinates)
        assert game_state_in_progress.target_x == int(coordinates.split(" ")[0])
        assert game_state_in_progress.target_y == int(coordinates.split(" ")[1])
