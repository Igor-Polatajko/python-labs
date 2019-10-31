#!/usr/bin/env python
from random import randint

variants = ["rock", "scissors", "paper"]


def generate_random_choice():
    return variants[randint(0, len(variants) - 1)]


def resolve_result(user_choice, program_choice):
    user_win_result = "You win! Congratulations... But it is only until I become AI."
    program_win_result = "I win! Maybe, next time will be more fortunate..."
    result = ""
    if user_choice not in variants:
        result = "I cannot get your input"
    elif user_choice == program_choice:
        result = "A draw"
    elif user_choice == "rock":
        if program_choice == "paper":
            result = program_win_result
        elif program_choice == "scissors":
            result = user_win_result
    elif user_choice == "paper":
        if program_choice == "scissors":
            result = program_win_result
        elif program_choice == "rock":
            result = user_win_result
    elif user_choice == "scissors":
        if program_choice == "rock":
            result = program_win_result
        elif program_choice == "paper":
            result = user_win_result
    return result


def main():
    print("Lest play scissors–rock–paper")
    print("Your input may be: 'scissors', 'rock', 'paper', 'stop' (to finish the game)")
    while True:
        user_choice = input("Enter your choice first (I will not cheat, I promise): ")
        if user_choice == "stop":
            break
        program_choice = generate_random_choice()
        print("My choice:", program_choice)
        print("Result:", resolve_result(user_choice, program_choice))
        print()


if __name__ == '__main__':
    main()
