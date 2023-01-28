from collections import deque
from termcolor import colored


def is_the_game_even(rows, cols):
    even_game = False
    for row in range(rows):
        found = False
        for col in range(cols):
            if matrix[row][col] == "X":
                found = True
                break
        if found:
            break
    else:
        even_game = True

    if even_game:
        print(colored("No winner, the game is even", 'red'))
        raise SystemExit


def get_color_coded_str(first, second, *args):
    result = ''
    for el in args:
        if el == first:
            result += f"\033[33m{el}\033[0m "
        elif el == second:
            result += f"\033[32m{el}\033[0m "
        else:
            result += "X "
    return result.strip()


rows, cols = 6, 7
matrix = [["X"] * cols for _ in range(rows)]

first_player_name = input("First player name: ")
second_player_name = input("Second player name: ")
first_player_symbol = first_player_name[0]
second_player_symbol = second_player_name[0] if first_player_symbol != second_player_name[0] else second_player_name[
                                                                                                      0] + '2'
turns = deque([first_player_name, first_player_symbol, second_player_name, second_player_symbol])
win = False

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, 1),
    (1, 1),
    (1, -1),
    (-1, -1),
)

while True:
    is_the_game_even(rows, cols)
    current_player, current_symbol = turns.popleft(), turns.popleft()
    turns.append(current_player)
    turns.append(current_symbol)
    available = True
    current_player_pos = []
    [print(get_color_coded_str(first_player_symbol, second_player_symbol, *x)) for x in matrix]

    try:
        player_turn = int(input(f"{current_player} choose a column: ")) - 1
    except ValueError:
        print(colored("Please type in a number!", 'red'))
        continue

    if not (0 <= player_turn < cols):
        print(colored(f"Invalid Column, between 1 and {cols}", 'red'))
        continue

    for row in range(rows - 1, -1, -1):
        if matrix[row][player_turn] == "X":
            matrix[row][player_turn] = current_symbol
            current_player_pos.append(row)
            current_player_pos.append(player_turn)
            break
    else:
        print(colored("No available spot! Choose another column", 'red'))
        available = False

    if not available:
        continue

    for direction in directions:
        r, c = current_player_pos[0] + direction[0], current_player_pos[1] + direction[1]
        if not 0 <= r < rows or not 0 <= c < cols:
            continue
        counter = 1

        for _ in range(3):
            if not 0 <= r < rows or not 0 <= c < cols:
                break
            if matrix[r][c] == current_symbol:
                counter += 1
            if counter == 4:
                [print(get_color_coded_str(first_player_symbol, second_player_symbol, *x)) for x in matrix]
                print(colored(f"{current_player} won the game!", 'red'))
                win = True
                break
            r += direction[0]
            c += direction[1]

        if win:
            break
    if win:
        break
