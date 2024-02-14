from game_state import GameState
import random
class TicTacToe():
    current_state: GameState
    
    def __init__(self):
        self.current_state = GameState()

    def start(self):
        if not self.is_user_move():
            self.make_move()
        self.draw_playground()
        while not self.is_over():
            self.ask_user()
            self.make_move()
            self.draw_playground()

    def draw_cell(self, with_left_border, content):
        return "| " + (content if content != None else " ") +  (" |" if with_left_border else " ")

    def draw_row(self, index, row_content):
        result =  f"{index} "
        for i in range(3):
         result += self.draw_cell(with_left_border=(i==2), content=row_content[i])
        result += "\n  -------------\n"
        return result
    
    def draw_playground(self):
        result = "    0   1   2  \n  -------------\n" 
        for i in range(3):
            result += self.draw_row(i, self.current_state.moves[i])
        print(result)
    
    def who_is_first_random(self):
        is_user_first = random.choice([True, False])
        if is_user_first:
            print("You are first!")
        else: print("I am first!")
        self.current_state.is_user_move = is_user_first
    
    def is_user_move(self):
        return self.current_state.is_user_move
    
    def is_over(self):
        return self.current_state.end_of_game
    
    def print_winner(self):
        if not self.current_state.win:
            print("The friendship wins!")
        else:
            if self.current_state.is_user_move:
                print("You win!") 
            else: print("I win!")

    def ask_user(self):
        coordinates = input('Enter coordinates of your move in format "x y": ').split(" ")
        self.current_state.target_x = int(coordinates[0])
        self.current_state.target_y = int(coordinates[1])
        self.current_state.is_user_move = True
        self.current_state.update()

    def make_move(self):
        if self.is_over():
            return
        x = None
        y = None
        x_options = set([0,1,2])
        coordinates_found = False
        while not coordinates_found and len(x_options) > 0:
            x = random.choice(list(x_options))
            x_options.remove(x)
            y_options = set([0,1,2])
            while not coordinates_found and len(y_options) > 0:
                y = random.choice(list(y_options))
                y_options.remove(y)
                if self.current_state.cell_is_empty(x, y):
                    coordinates_found = True
        self.current_state.target_x = x
        self.current_state.target_y = y
        self.current_state.is_user_move = False
        self.current_state.update()



    
    def coordinates_validated(self, coordinates):
        return False if self.current_state.moves[int(coordinates[0])][int(coordinates[1])] != None else True
    