#!/usr/bin/env python
import random

WINNING_POS = [(0, 1, 2), (3, 4, 5),
               (6, 7, 8), (0, 3, 6),
               (1, 4, 7), (2, 5, 8),
               (0, 4, 8), (2, 4, 6)]


def draw_field(field):
    assert len(field) == 9
    print("\n------- Field -----")
    for i in range(0, 3):
        base_row_ind = i * 3
        print(f"{field[base_row_ind]} {field[base_row_ind + 1]} {field[base_row_ind + 2]}")


def draw_winning_result(is_user_win):
    print("\n\n**********************************")
    if is_user_win:
        print("*  Congratulations, you win!!!!  *")
    else:
        print("* You lose! AI proved its power! *")
    print("**********************************")


def is_user_start_first():
    return random.randint(0, 2) % 2


def get_user_choice(field_state):
    while True:
        try:
            user_choice = int(input("Enter your choice: "))
            if 9 < user_choice or user_choice < 1:
                print("Position out of bounds")
                raise ValueError
            if field_state[user_choice - 1] != '-':
                print("Position is already filled")
                raise ValueError
            return user_choice
        except ValueError:
            print("Incorrect input!")


def is_winning_pos(field_state, sym):
    for wp in WINNING_POS:
        if field_state[wp[0]] == field_state[wp[1]] == field_state[wp[2]] == sym:
            return True
    return False


def get_indexes_in_list(data, sym):
    return [i for i, item in enumerate(data) if item == sym]


def get_computer_choice(field_state, sym):
    potential_choices = get_indexes_in_list(field_state, '-')
    filled_by_current_sym = get_indexes_in_list(field_state, sym)

    for wp in WINNING_POS:
        win_set = set(wp)
        good_choices = win_set - set(filled_by_current_sym)
        if len(good_choices) == 1 and list(good_choices)[0] in potential_choices:
            return list(good_choices)[0] + 1

    return random.choice(potential_choices) + 1


def game_loop():
    print("\n##### Game started #####")
    field_state = ['-' for _ in range(1, 10)]
    draw_field(field_state)
    is_user_turn = is_user_start_first()
    current_sym = 'X'
    while True:
        if is_user_turn:
            print(' @@ Now is your turn: @@')
            next_step = get_user_choice(field_state)
        else:
            print(' @@ Computer\'s turn: @@')
            next_step = get_computer_choice(field_state, current_sym)

        field_state[next_step - 1] = current_sym
        draw_field(field_state)

        if is_winning_pos(field_state, current_sym):
            draw_winning_result(is_user_turn)
            break

        is_user_turn = not is_user_turn
        current_sym = 'O' if current_sym == 'X' else 'X'


def show_game_rules():
    print("\nHere are the position indexes:")
    draw_field([x for x in range(1, 10)])


if __name__ == '__main__':
    show_game_rules()
    game_loop()
