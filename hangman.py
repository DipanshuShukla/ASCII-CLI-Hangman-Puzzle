import random

with open('sowpods.txt', 'r') as FILE:
    WORDS = FILE.read().split("\n")


def NewWord():
    return random.choice(WORDS)


def getInput(lst):
    inpt = input("Enter your guess - ").upper()
    while True:
        if len(inpt) != 1 or inpt.isdigit() or inpt in '[@_!#$%^&*()<>?/\|}{~:]':
            inpt = input("INVALID INPUT\nInput should be a single letter\nEnter your guess - ").upper()
        elif inpt in lst:
            inpt = input("You already guessed \"{}\"\nEnter your guess - ".format(inpt)).upper()
        else:
            return inpt


def game():
    word = NewWord()
    print(word)

    lives = 6
    chosenLetters = []
    screenWord = "-" * len(word)

    while True:

        found = False

        print(screenWord + "\nlives left = {}".format(lives))
        if lives > 0:
            if screenWord == word:
                print("Congratulation!! You Won!")
                break

            inpt = getInput(chosenLetters)
            chosenLetters.append(inpt)

            for i in range(len(word)):
                if word[i] == inpt:
                    screenWord = screenWord[:i] + inpt + screenWord[i + 1:]
                    found = True
            if not found:
                lives -= 1
        else:
            print("You lost!")
            break

    if input("Play again? (y/n) ").lower() == "y":
        game()
        return
    else:
        print("Goodbye.")
        return


if __name__ == '__main__':
    game()
