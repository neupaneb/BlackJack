import os
import random
import sys

# Initialize deck of cards: numbers 2-10 and face cards (J, Q, K) all valued at 10, and Aces valued at 11.
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal(deck):
    """Deal two cards from the deck and return as a hand."""
    hand = []
    for _ in range(2):
        card = deck.pop()
        if card == 11:
            card = "A"
        elif card == 10:
            card = random.choice(["J", "Q", "K"])
        hand.append(card)
    return hand

def play_again():
    """Ask the user if they want to play again and reset the deck if so."""
    again = input("Do you want to play again? (Y/N): ").lower()
    if again == "y":
        global deck
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        game()
    else:
        print("Bye!")
        sys.exit()

def total(hand):
    """Calculate the total value of a hand."""
    total = 0
    num_aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            num_aces += 1
            total += 11
        else:
            total += card
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

def hit(hand):
    """Draw a card from the deck and add it to the hand."""
    card = deck.pop()
    if card == 11:
        card = "A"
    elif card == 10:
        card = random.choice(["J", "Q", "K"])
    hand.append(card)
    return hand

def clear():
    """Clear the console screen."""
    if os.name == 'nt':  # For Windows
        os.system('CLS')
    elif os.name == 'posix':  # For Unix/Linux/Mac
        os.system('clear')

def print_results(dealer_hand, player_hand):
    """Print the results of the game."""
    clear()
    print(f"The dealer has a {dealer_hand} for a total of {total(dealer_hand)}")
    print(f"You have a {player_hand} for a total of {total(player_hand)}")

def blackjack(dealer_hand, player_hand):
    """Check for Blackjack and print the result."""
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
        play_again()

def score(dealer_hand, player_hand):
    """Determine and print the final score based on hands."""
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Congratulations! You got a Blackjack!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you lose. The dealer got a blackjack.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry. You busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busts. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry. Your score isn't higher than the dealer. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Congratulations. Your score is higher than the dealer. You win!\n")

def game():
    """Main game loop."""
    choice = ""
    clear()
    print("WELCOME TO BLACKJACK!\n")
    global deck
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print(f"The dealer is showing a {dealer_hand[0]}")
        print(f"You have a {player_hand} for a total of {total(player_hand)}")
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        clear()
        if choice == "h":
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print("Bye!")
            sys.exit()

if __name__ == "__main__":
    game()
