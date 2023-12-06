
import os
import art
from art import logo

def clear_terminal():
    # Print 100 empty lines to simulate clearing the console
    print('\n' * 100)

# Print something to the console
print("This is some output.")

# Call the function to clear the terminal
print(logo)
print("Welcome to the secret auction program.")
bidders = {}
should_continue = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"Winner is {winner} with a bid of ${bid_amount}")
while should_continue:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: "))
    bidders[name] = bid_amount
    question = input("Are there any other bidders? (yes/no): ").lower()

    if question == 'no':
        should_continue = False
        find_highest_bidder(bidders)
    elif question == 'yes':
        # Clear the terminal before taking the next bid
        clear_terminal()




