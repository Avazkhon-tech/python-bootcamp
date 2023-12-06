from game_data import data
from random import choice, randint
from art import vs


def get_random_num():
    """returns a ramdom number"""
    random_num = randint(0, len(data)-1)
    return random_num


def return_random_person(list_people, number, beggining_text):
    """return formatted text about the person"""
    random_person = list_people[number]
    return f"{beggining_text} {random_person['name']}, {random_person['description']}, from {random_person['country']}"


text_1 = 'Compare A: '
text_2 = 'Against B: '

def compare_numbers(data, num1, num2):
    higher_num_letter = ''
    num1 = data[num1]['follower_count']
    num2 = data[num2]['follower_count']
    if num1 > num2:
        higher_num_letter = 'a'
    else:
        higher_num_letter = 'b'
    return higher_num_letter


def game():
    score = 0
    num_1 = get_random_num()
    while True:
        num_2 = get_random_num()
        while num_1 == num_2:
            num_2 = get_random_num()

        print(return_random_person(data, num_1, text_1))
        print(vs)
        print(return_random_person(data, num_2, text_2))

        letter_for_higher = compare_numbers(data, num_1, num_2)
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if letter_for_higher == user_input:
            score += 1
            print(f"You are right! Your current score: {score}")
        else:
            print('You lost, your score: ', score)
            break
        num_1 = num_2


game()