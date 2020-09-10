def chk_empty(cell):
    for x in cell:
        if x == " ":
            return False
    return True


def print_cell(cell):
    print('---------')
    for i in range(0, 7, 3):
        print("| {} {} {} |".format(cell[i], cell[i + 1], cell[i + 2]))
    print('---------')


def chk_field(cell):
    global state
    x_win = 0
    o_win = 0
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for a, b, c in win_patterns:
        if (cell[a], cell[b], cell[c]) == ('X', 'X', 'X'):
            x_win += 1
        if (cell[a], cell[b], cell[c]) == ('O', 'O', 'O'):
            o_win += 1

    if x_win > 0 and o_win > 0 or abs(cell.count('X') - cell.count('O')) == 2:
        state = 'Impossible'
    elif x_win == 1:
        state = 'X wins'
    elif o_win == 1:
        state = 'O wins'
    elif chk_empty(cell) is True:
        state = 'Draw'
    else:
        state = 'Game not finished'


def play():
    global cells
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
                    if cells[index_val] == " ":
                        if cells.count("X") > cells.count("O"):
                            cells[index_val] = "O"
                        else:
                            cells[index_val] = "X"
                        print_cell(cells)
                        flag = False
                    else:
                        print("This cell is occupied! Choose another one!")
                        flag = True
                        continue
                index_val += 1


cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print_cell(cells)
state = 'Game not finished'
while state == 'Game not finished':
    play()
    chk_field(cells)
print(state)

