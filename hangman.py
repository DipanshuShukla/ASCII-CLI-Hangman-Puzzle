import random
def GetWordFromFile(fileName):
    with open(fileName, 'r') as open_file:
        all_text = open_file.read()
        wordList = all_text.split("\n")
        word = random.choice(wordList)
    return word
def IsGuessedLetter(_guessedLetters, letter):
    if letter in _guessedLetters:
        return True
    else:
        return False
def UpdatePlayWord(_target, _guess, _display):    
    for index, x in enumerate(_target):
        if x == _guess.upper():
            _display[index * 2] = x
    return "".join(_display)
def GetPlayResult(_display, _attempts):
    if "_" not in _display:
        return "Congratulation on guessing all letters attempting " + str(_attempts) + "times."
    else:
        return "You have " + str(6 - _attempts) + " attempts left."
def IsEndOfGame(_target, _display, _attempts):
    if "_" not in _display or _attempts == 6:
        print("Target word is: " + _target + "\n")
        return True
    else:
        return False
def StartGame():
    print("Welcome to Hangman!")
    print("-------------------")
    return GetWordFromFile("sowpods.txt")
def InitializePlayLetters(_target):
    return list(len(_target) * "_ ") 
def IsValidInput(_userInput):
    if _userInput.isalpha(): return True
    else: return False
def PlayHangman():
    while True:
        target, guess, guessedLetters = "", "", set()    
        target = StartGame()
        display = InitializePlayLetters(target)
        while not IsEndOfGame(target, display, len(guessedLetters)):    
            guess = input("Guess your letter. 0 to exit: ")
            if IsValidInput(guess):
                if IsGuessedLetter(guessedLetters, guess):
                    print ("Already tried " + guess.upper())
                    print(GetPlayResult(display, len(guessedLetters)))
                else:
                    guessedLetters.add(guess)
                    if guess.upper() in set(target):
                        print((UpdatePlayWord(target, guess, display)))
                        print(GetPlayResult(display, len(guessedLetters)))                    
                    else: print(GetPlayResult(display, len(guessedLetters)))
                    if IsEndOfGame(target, display, len(guessedLetters)): break
            else:
                if guess == "0": break
        if guess == "0": break
def main():
    PlayHangman()
if __name__ == "__main__":
    main()
