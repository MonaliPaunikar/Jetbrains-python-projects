class Game:

    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.state = 'Game not finished'

    @staticmethod
    def chk_empty(cell):
        for x in cell:
            if x == " ":
                return False
        return True

    @staticmethod
    def print_cell(cell):
        print('---------')
        for i in range(0, 7, 3):
            print("| {} {} {} |".format(cell[i], cell[i + 1], cell[i + 2]))
        print('---------')


    def chk_field(self, cell):
        x_win = 0
        o_win = 0
        win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for a, b, c in win_patterns:
            if (cell[a], cell[b], cell[c]) == ('X', 'X', 'X'):
                x_win += 1
            if (cell[a], cell[b], cell[c]) == ('O', 'O', 'O'):
                o_win += 1

        if x_win > 0 and o_win > 0 or abs(cell.count('X') - cell.count('O')) == 2:
            self.state = 'Impossible'
        elif x_win == 1:
            self.state = 'X wins'
        elif o_win == 1:
            self.state = 'O wins'
        elif self.chk_empty(cell) is True:
            self.state = 'Draw'
        else:
            self.state = 'Game not finished'
        return self.state


    def play(self):
        flag = True
        while flag:
            coordinates = input('Enter the coordinates: >').split()
            flag = False
            if coordinates[0].isalpha() or coordinates[1].isalpha():
                print("You should enter numbers!")
                flag = True
                continue
            if not (0 < int(coordinates[0]) <= 3) or not (0 < int(coordinates[1]) <= 3):
                print("Coordinates should be from 1 to 3!")
                flag = True
                continue
            index_val = 0
            for row in range(1, 4):
                for col in range(1, 4):
                    if col == int(coordinates[0]) and row == int(coordinates[1]):
                        if self.cells[index_val] == " ":
                            if self.cells.count("X") > self.cells.count("O"):
                                self.cells[index_val] = "O"
                            else:
                                self.cells[index_val] = "X"
                            self.print_cell(self.cells)
                            flag = False
                        else:
                            print("This cell is occupied! Choose another one!")
                            flag = True
                            continue
                    index_val += 1
    
    def main(self):
        self.print_cell(self.cells)
        while self.state == 'Game not finished':
            self.play()
            self.chk_field(self.cells)
        print(self.state)

my_game = Game()
my_game.main()
