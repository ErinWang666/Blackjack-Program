import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def choose_card():
    rand_card = random.randint(0, 12)
    return cards[rand_card]

computer_cards = []
user_cards = []

computer_cards.append(choose_card())
computer_cards.append(choose_card())
computer_sum = sum(computer_cards)
print(f"The computer's cards are {computer_cards}.")
print(f"The total of the computer's cards is {computer_sum}.")

user_cards.append(choose_card())
continue_choose = True
while continue_choose == True:
    user_cards.append(choose_card())
    if sum(user_cards) > 21:
        if 11 in user_cards:
            user_cards.remove(11)
            user_cards.append(1)
        else:
            continue_choose = False
    user_sum = sum(user_cards)
    print(f"Your cards are {user_cards}.")
    print(f"The total of your cards is {user_sum}.")
    if continue_choose == False:
        print("You lose.")
    else:
        con_choose = input("Would you like to choose another card? Type 'y' or 'n'. ").lower()
        if con_choose == 'y':
            continue_choose = True
        else:
            continue_choose = False

if user_sum <= 21:
    if user_sum < computer_sum:
        print("You lose.")
    elif user_sum > computer_sum:
        print("You win.")
    elif user_sum == computer_sum:
        print("You draw.")