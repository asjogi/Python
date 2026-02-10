import random as rd
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
# my_cards = []
# my_cards.insert(0,rd.choice(cards))
# my_cards.insert(1,rd.choice(cards))

# print(rd.choice(cards))
# print(sum(my_cards))
# my_cards = []
# comp_cards = []


def black_jack():
    play_game = str(input("Do you want to play black jack ? 'Y' or 'N' : ")).upper()
    while play_game == 'Y':
        my_cards = []
        comp_cards = []
        my_cards.insert(0,rd.choice(cards))
        my_cards.insert(1,rd.choice(cards))
    #
        comp_cards.insert(0,rd.choice(cards))
    #
        print(f"Your cards: {my_cards} \nComputer's first card: {comp_cards}" )
        play_continue = str(input("Type 'Y' to get another card, type 'n' to pass: ")).lower()
        comp_cards.insert(1,rd.choice(cards))
    #
        if play_continue == 'n' and sum(comp_cards) < 17:
            comp_cards.insert(2,rd.choice(cards))
            print(f"comp cards 1 :{comp_cards}")
        elif sum(my_cards) < 17: 
            my_cards.insert(2,rd.choice(cards))
            print(f"my cards less than 17 :{my_cards}")
        if sum(comp_cards) < 17:
            comp_cards.insert(2,rd.choice(cards))
            print(f"comp cards less than 17 :{comp_cards}")
        if sum(comp_cards) <= 21 and sum(comp_cards) > sum(my_cards):
            print("Computer win !!")
        elif sum(my_cards) <= 21 and sum(comp_cards) < sum(my_cards):
            print("You win !!")
        elif sum(comp_cards) == sum(my_cards):
            print("It's a draw !!")
        elif sum(comp_cards) > 21 :
            print("You win !!")
        else:
            print("Computer win !!")
        black_jack()


black_jack()
