import random

word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")

while True:
    choice = input('Type "play" to play the game, "exit" to quit:')
    valid_options = ("play", "exit")
    if choice not in valid_options:
        continue
    if choice == "exit":
        break
    if choice == "play":
        computer_choice = random.choice(word_list)
        guessed = set()
        trial = 1
        word = list('-' * len(computer_choice))

        while trial <= 8:
            print()
            print("".join(word))
            letter = input("Input a letter:")
            index_list = []
            if len(letter) != 1:
                print("You should input a single letter")
                continue
            if letter.islower() is False:
                print("It is not an ASCII lowercase letter")
                continue
            if letter in guessed:
                print("You already typed this letter")
                continue
            if letter in computer_choice:
                for x in range(len(computer_choice)):
                    if computer_choice[x] == letter:
                        index_list.append(x)
                for y in index_list:
                    word[y] = letter
                guessed.add(letter)
                if "-" not in word:
                    print("You guessed the word!\nYou survived!")
                    break
            else:
                guessed.add(letter)
                print("No such letter in the word")
                trial += 1

        if trial > 8 and "-" in word:
            print("You are hanged!")