game_list = list('         ')
x_lst = ['x', 'x', 'x']
o_lst = ['o', 'o', 'o']
winner = ''
win = False
impossible = False
finished = False


def count(lst):
    x = sum([1 for ele in lst if ele == 'x'])
    o = sum([1 for ele in lst if ele == 'o'])
    return abs(x - o) > 1


def game_board():
    print('---------')
    print('|', game_list[0].upper(), game_list[1].upper(), game_list[2].upper(), '|')
    print('|', game_list[3].upper(), game_list[4].upper(), game_list[5].upper(), '|')
    print('|', game_list[6].upper(), game_list[7].upper(), game_list[8].upper(), '|')
    print('---------')


def error_check():
    while True:
        try:
            user_move = list(input('Please enter the coordinates of the space you would like to play on: ').split(' '))
            row = int(user_move[0])
            column = int(user_move[1])
            assert 0 < row <= 3 and 0 < column <= 3
        except ValueError:
            print("You should enter numbers!")
        except AssertionError:
            print("Coordinates should be from 1 to 3!")
        else:
            index = (((row - 1) * 3) + (column + 2)) - 3
            if game_list[index] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                return index


def player_1_turn():
    global game_list
    board_index = error_check()
    game_list[board_index] = 'x'
    return game_list


def player_2_turn():
    global game_list
    board_index = error_check()
    game_list[board_index] = 'o'
    return game_list


def win_check():
    global win
    global winner
    if game_list[0:3] == x_lst or game_list[3:6] == x_lst or game_list[6:9] == x_lst:
        winner += 'X'
        win = True
    elif game_list[0:3] == o_lst or game_list[3:6] == o_lst or game_list[6:9] == o_lst:
        winner += 'O'
        win = True
    elif game_list[0:7:3] == x_lst or game_list[1:8:3] == x_lst or game_list[2:9:3] == x_lst:
        winner += 'X'
        win = True
    elif game_list[0:7:3] == o_lst or game_list[1:8:3] == o_lst or game_list[2:9:3] == o_lst:
        winner += 'O'
        win = True
    elif game_list[0:9:4] == x_lst or game_list[2:7:2] == x_lst:
        winner += 'X'
        win = True
    elif game_list[0:9:4] == o_lst or game_list[2:7:2] == o_lst:
        winner += 'O'
        win = True
    return win, winner


def impossible_check():
    global impossible
    if game_list[0:3] == x_lst or game_list[3:6] == x_lst or game_list[6:9] == x_lst:
        if game_list[0:3] == o_lst or game_list[3:6] == o_lst or game_list[6:9] == o_lst:
            impossible = True
    elif game_list[0:7:3] == x_lst or game_list[1:8:3] == x_lst or game_list[2:9:3] == x_lst:
        if game_list[0:7:3] == o_lst or game_list[1:8:3] == o_lst or game_list[2:9:3] == o_lst:
            impossible = True
    elif game_list[0:9:4] == x_lst or game_list[2:7:4] == x_lst:
        if game_list[0:9:4] == o_lst or game_list[2:7:4] == o_lst:
            impossible = True
    elif count(game_list):
        impossible = True
    return impossible


def play_game():
    player_1_turn()
    game_board()
    win_check()
    impossible_check()
    if impossible:
        print('Impossible')
        return
    elif win:
        print(f'{winner} wins')
        return
    elif ' ' not in game_list and not win:
        print('Draw')
        return
    player_2_turn()
    game_board()
    win_check()
    impossible_check()
    if impossible:
        print('Impossible')
        return
    elif win:
        print(f'{winner} wins')
        return
    elif ' ' not in game_list and not win:
        print('Draw')
        return


game_board()
while ' ' in game_list and not win:
    play_game()