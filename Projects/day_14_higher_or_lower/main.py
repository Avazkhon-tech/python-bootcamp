from game_data import data
from random import choice, randint
from art import vs, logo

#
# def get_random_num():
#     """returns a ramdom number"""
#     random_num = randint(0, len(data)-1)
#     return random_num
#
#
# def return_random_person(list_people, number, beginning_text):
#     """return formatted text about the person"""
#     random_person = list_people[number]
#     return f"{beginning_text} {random_person['name']}, {random_person['description']}, from {random_person['country']}"
#
#
# text_1 = 'Compare A: '
# text_2 = 'Against B: '
#
#
# def compare_numbers(data, num1, num2):
#     higher_num_letter = ''
#     num1 = data[num1]['follower_count']
#     num2 = data[num2]['follower_count']
#     if num1 > num2:
#         higher_num_letter = 'a'
#     else:
#         higher_num_letter = 'b'
#     return higher_num_letter
#
#
# def game():
#     score = 0
#     num_1 = get_random_num()
#     while True:
#         print(logo)
#         num_2 = get_random_num()
#         while num_1 == num_2:
#             num_2 = get_random_num()
#
#         print(return_random_person(data, num_1, text_1))
#         print(vs)
#         print(return_random_person(data, num_2, text_2))
#
#         letter_for_higher = compare_numbers(data, num_1, num_2)
#         user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
#         if letter_for_higher == user_input:
#             score += 1
#             print(f"You are right! Your current score: {score}")
#         else:
#             print('You lost, your score: ', score)
#             break
#         num_1 = num_2
#
#
# game()


# angela's solution


def format_data(account):
    """format the account data into a printable data."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


# display art
game_should_continue = True
score = 0
account_b = choice(data)
while game_should_continue:
    print(logo)
    # generate a random account from the game data list
    account_a = account_b
    account_b = choice(data)

    while account_a == account_b:
        account_b = choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? 'A', 'B': ").lower()

    # check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print("Sorry, that's wrong.")
        break


# get follower count of each account
# use if statement to check if user is correct
# give user feedback on their guess

# making the account at position b become the next account at position a

# clear the screen













