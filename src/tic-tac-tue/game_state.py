from pydantic import BaseModel, Field
from typing import List, Optional


class GameState(BaseModel):
    target_x: int = Field(ge=0, lt=3, default=None)
    target_y: int = Field(ge=0, lt=3, default=None)
    is_user_move: bool = Field(default=False)
    moves: List[List[str]] = Field(
        default = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
            ])
    end_of_game: bool = Field(default=False)
    win: bool = Field(default=False)
    filled_cells_count: int = Field(default=0)



    def check_if_win(self):
        for i in range(3):
            if self.check_row(i):
                self.end_of_game = True
                self.win = True
                return
            if self.check_column(i):
                self.end_of_game = True
                self.win = True
                return
        if self.check_diagonals():
            self.win = True
            self.end_of_game = True

    
    def update(self):
        content = "x" if self.is_user_move else "o"
        self.moves[self.target_x][self.target_y] = content
        self.filled_cells_count += 1
        self.check_if_win()
        if self.filled_cells_count == 9:
            self.end_of_game = True 

    def cell_is_empty(self, x, y):
        return self.moves[x][y] == None    


    def check_row(self, i):
        return self.moves[i][0] == self.moves[i][1] == self.moves[i][2] != None

    def check_column(self, j):
        return self.moves[0][j] == self.moves[1][j] == self.moves[2][j] != None

    def check_diagonals(self):
        return self.moves[0][0] == self.moves[1][1] == self.moves[2][2] != None or \
        self.moves[0][2] == self.moves[1][1] == self.moves[2][0] != None
