import random

def game_decorator(func):
    def wrapper(user_choice):
        game_images = [
            '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            ''',
            '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            ''',
            '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''
        ]

        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice >= 3 or user_choice < 0:
            return "You typed an invalid number, you lose!"
        elif user_choice == 0 and computer_choice == 2:
            return "You win!"
        elif computer_choice == 0 and user_choice == 2:
            return "You lose"
        elif computer_choice > user_choice:
            return "You lose"
        elif user_choice > computer_choice:
            return "You win!"
        elif computer_choice == user_choice:
            return "It's a draw"

    return wrapper


@game_decorator
def play_game(user_choice):
    return user_choice


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
result = play_game(user_choice)
print(result)
