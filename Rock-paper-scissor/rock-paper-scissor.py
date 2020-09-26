import random

class game:

    def __init__(self):
        self.score = 0

    def default_game(self, user_choice):
        game_option = ['rock', 'paper', 'scissors']
        option = random.choice(game_option)
        check_win = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
        if check_win[user_choice] == option:
            print(f'Well done. Computer chose {option} and failed')
            self.score += 100
        elif user_choice == option:
            print(f'There is a draw {option}')
            self.score += 50
        else:
            print(f'Sorry, but computer chose {option}')

    def game(self, user_option, user_choice):
        option = random.choice(user_option)
        length = len(user_option)
        mid = length // 2
        while user_option.index(user_choice) != mid:
            user_option.insert(0, user_option[length-1])
            user_option.pop(length)
        win = user_option[:mid]
        check_win = {user_choice: win}
        if user_choice == option:
            print(f'There is a draw {option}')
            self.score += 50
        elif option in check_win[user_choice]:
            print(f'Well done. Computer chose {option} and failed')
            self.score += 100
        else:
            print(f'Sorry, but computer chose {option}')

    def check_input(self, options, user_input):
        valid_input = ['!exit', '!rating', 'rock', 'paper', 'scissors']
        valid_input.extend(options)
        if user_input in valid_input:
            return True
        return False

    def menu(self, options):
        print("Select any of the following option:")
        total_options = ['!exit', '!rating', 'rock', 'paper', 'scissors']
        if len(options) > 1:
            total_options.extend(options)
        print(total_options)
        print('Enter your choice:')


    def main(self):
        user = input("Enter your name: ")
        print(f"Hello {user}")
        my_file = open('rating.txt')
        my_list = []
        for line in my_file:
            data = line.split()
            my_list.append(data)
        for record in my_list:
            if record[0] == user:
                self.score = int(record[1])
                break
        print("Enter the options you want to play with seperated by comma(,). To play with default options(rock, paper, scissors), press enter:")
        options = input().split(",")
        print("Okay, let's start")
        while True:
            self.menu(options)
            user_input = input()
            if self.check_input(options, user_input) is False:
                print("Invalid Input")
                continue
            if user_input == '!exit':
                print("Bye!")
                break
            if user_input == '!rating':
                print(f"Your rating: {self.score}")
                continue
            if len(options) > 1:
                self.game(options, user_input)
            else:
                self.default_game(user_input)
        my_file.close()

my_game = game()
my_game.main()