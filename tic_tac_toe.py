from collections import deque


def win_func(symbol):
    first_diagonal_win = all([matrix[i][i] == symbol for i in range(size)])
    second_diagonal_win = all([matrix[i][size - 1 - i] == symbol for i in range(size)])
    row_win = any([all(True if pos == symbol else False for pos in row) for row in matrix])
    col_win = any([all(True if matrix[r][c] == symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        return True
    return False


def print_func(player, begin):
    if begin:
        print("This is the numeration of the board")
        [print(f'| {" | ".join(row)} |') for row in matrix]
        print(f'{player} starts first!')

        for row in range(size):
            for col in range(size):
                matrix[row][col] = ''
    else:
        [print(f'| {" | ".join(row)} |') for row in matrix]


player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
player_one_symbol = input(f'{player_one_name} choose a symbol: "X" or "O" ').upper()

while player_one_symbol not in ["X", "O"]:
    player_one_symbol = input(f'{player_one_name} choose a symbol: "X" or "O" ').upper()

player_two_symbol = "X" if player_one_symbol == "O" else "O"
turns = deque([player_one_name, player_one_symbol, player_two_name, player_two_symbol])
size = 3
matrix = [[str(row), str(row + 1), str(row + 2)] for row in range(1, 10, 3)]
begin = True

while True:

    current_player, current_symbol = turns.popleft(), turns.popleft()
    turns.append(current_player)
    turns.append(current_symbol)
    print_func(current_player, begin)
    begin = False
    try:
        position = int(input(f'{current_player} choose a free position from 1 to 9 '))
    except ValueError:
        print("Please enter a number from 1 to 9!")
        continue

    row, col = (position - 1) // 3, (position - 1) % 3
    matrix[row][col] = current_symbol
    win = win_func(current_symbol)

    if win:
        print_func(current_player, begin)
        print(f"{current_player} won the game!")
        break
