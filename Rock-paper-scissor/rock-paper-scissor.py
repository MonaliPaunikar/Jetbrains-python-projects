import random


def default_result(user_choice):
    global score
    game_option = ['rock', 'paper', 'scissors']
    option = random.choice(game_option)
    check_win = {'scissors': 'paper', 'paper': 'rock', 'rock': 'scissors'}
    if check_win[user_choice] == option:
        print(f'Well done. Computer chose {option} and failed')
        score += 100
    elif user_choice == option:
        print(f'There is a draw {option}')
        score += 50
    else:
        print(f'Sorry, but computer chose {option}')


def result(user_option, user_choice):
    global score
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
        score += 50
    elif option in check_win[user_choice]:
        print(f'Well done. Computer chose {option} and failed')
        score += 100
    else:
        print(f'Sorry, but computer chose {option}')


user = input("Enter your name: ")
print(f"Hello, {user}")
my_file = open('rating.txt', 'r')
my_list = []
for line in my_file:
    data = line.split()
    my_list.append(data)
score = 0
for record in my_list:
    if record[0] == user:
        score = int(record[1])
        break
options = input().split(",")
print("Okay, let's start")
while True:
    user_input = input()
    valid_input = ['!exit', '!rating', 'rock', 'paper', 'scissors']
    valid_input.extend(options)
    if user_input not in valid_input:
        print("Invalid input")
        continue
    if user_input == '!exit':
        print("Bye!")
        break
    if user_input == '!rating':
        print(f"Your rating: {score}")
        continue
    if len(options) > 1:
        result(options, user_input)
    else:
        default_result(user_input)
my_file.close()
