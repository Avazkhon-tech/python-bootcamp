logo = """
 ,-.                  .   .                      .           
/                     |   |                      |           
| -. . . ,-. ,-. ,-.  |-  |-. ,-.  ;-. . . ;-.-. |-. ,-. ;-. 
\  | | | |-' `-. `-.  |   | | |-'  | | | | | | | | | |-' |   
 `-' `-` `-' `-' `-'  `-' ' ' `-'  ' ' `-` ' ' ' `-' `-' '                  
"""
                                                                                                               

print(logo)


def game():
    import random
    random_number = random.randint(1, 100)
    attempts = 0

    def greet():
        """Greets the user"""
        print("Welcome to the Number Guessing Game!"
              "\nI am thinking of a number beetween 1 and 100.")
        
    def game_level():
        """Returns the number of attempts based on the level of the game"""
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level.lower() == 'easy':
            return 10
        elif level.lower() == 'hard':
            return 5
        else:
            print("Run the game again and enter valid value!")

    def check_guess(random_num, attempts):
        while attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            user_attempt = int(input("Make a guess: "))

            if user_attempt == random_num:
                print(f"You got it! The answer is {user_attempt}")
                break
            elif user_attempt > random_num:
                print("Too high")
            else:
                print("Too low")
            attempts -= 1
            if attempts == 0:
                print("You lose")
    greet()
    attempts = game_level()
    check_guess(random_number, attempts)
game()



















