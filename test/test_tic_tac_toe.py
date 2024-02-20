import pytest
import re


@pytest.mark.parametrize("with_left_border, content, result",
                         [
                             (True, "x", "| x |"),
                             (False, "x", "| x "),
                             (True, "o", "| o |"),
                             (False, "o", "| o "),
                             (True, None, "|   |"),
                             (False, None, "|   ")
                         ])
def test_draw_cell(tic_tac_toe, with_left_border, content, result):
    assert tic_tac_toe.draw_cell(with_left_border, content) == result

@pytest.mark.parametrize("index, row_content, result",
                         [
                             (0, [None, "x", "o"], "0 |   | x | o |\n  -------------\n"),
                             (1, [None, None, None], "1 |   |   |   |\n  -------------\n"),
                             (2, ["o", "o", "x"], "2 | o | o | x |\n  -------------\n"),
                         ])
def test_draw_row(tic_tac_toe, index, row_content, result):
    assert tic_tac_toe.draw_row(index, row_content) == result

def test_calculate_coordinates(tic_tac_toe):
    assert re.fullmatch(r"[0-2] [0-2]", tic_tac_toe.calculate_coordinates()) != None