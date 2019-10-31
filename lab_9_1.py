#!/usr/bin/env python

CARDS_VALUES = dict.fromkeys(['T', 'J', 'Q', 'K'], 10)


def calc_cards_sum(cards_list):
    sum = 0
    count_A = 0
    for card in cards_list:
        if str(card).isdigit() and 2 <= int(card) <= 10:
            sum += int(card)
        elif card in CARDS_VALUES.keys():
            sum += CARDS_VALUES[card]
        elif card == 'A':
            count_A += 1

    for i in range(0, count_A):
        if sum + count_A + 11 <= 21:
            sum += 11
        else:
            sum += 1
        count_A -= 1
    return sum


if __name__ == '__main__':
    cards = input("Enter cards: ")
    cards_sum = calc_cards_sum(cards.split())
    if cards_sum <= 21:
        print(f"Cards sum: {cards_sum}")
    else:
        print("Bust")
