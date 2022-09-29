import random
import string

games_won = 0
games_lost = 0


def play_game():
    word_list = ['python', 'java', 'swift', 'javascript']
    word = random.choice(word_list)
    initial_board = ('-' * len(word))
    attempts = 8
    game_over = False
    win = False
    board = list('-' * len(word))
    tracker = set()
    alpha_lower = list(string.ascii_lowercase)
    global games_won
    global games_lost

    print(initial_board)
    print()

    while not game_over:
        if attempts <= 0:
            game_over = True
        if '-' not in board:
            win = True
        if win:
            games_won += 1
            print(f'You guessed the word {word}!')
            print('You survived!')
            main_menu()
            break
        if game_over:
            games_lost += 1
            print('You lost!')
            main_menu()
            break
        player_guess = input('Input a letter: ')
        if len(list(player_guess)) > 1 or player_guess == "":
            print('Please, input a single letter')
            print()
            print(''.join(board))
            continue
        elif player_guess not in alpha_lower:
            print('Please, enter a lowercase letter from the English alphabet')
            print()
            print(''.join(board))
            continue
        elif player_guess in tracker:
            print("You've already guessed this letter")
            print()
            print(''.join(board))
            continue
        elif player_guess not in set(word):
            attempts -= 1
            tracker.add(player_guess)
            print("That letter doesn't appear in the word.\n")
            print()
            print(''.join(board))
        elif player_guess in set(word):
            for i, l in enumerate(word):
                if player_guess == l:
                    tracker.add(player_guess)
                    board[i] = l
                    print()
                    print(''.join(board))


def main_menu():
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    valid_choices = {'play', 'results', 'exit'}
    global games_won
    global games_lost

    while True:
        while menu not in valid_choices:
            menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if menu == 'play':
            play_game()
        if menu == 'results':
            print(f'You won: {games_won} times.')
            print(f'You lost: {games_lost} times.')
            menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if menu == 'exit':
            exit()


print('H A N G M A N')
main_menu()
