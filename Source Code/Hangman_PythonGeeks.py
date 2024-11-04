#PythonGeeks- imports
import random
import time

#PythonGeeks- Initial Steps to invite in the game:
print("\n\n***  Welcome to Hangman game by PythonGeeks  ***\n")
name = input("Enter your name: ")
print("Good Luck!", name)
time.sleep(2)
print("LET'S PLAY HANGMAN! A word will be chosen randomly. You will have to guess it!\n")
time.sleep(3)

#PythonGeeks: Parameters required for the excution of game
def main():
    global word
    global count    
    global length
    global display
    global alreadyGuessed
    global playGame
    
    words = ['programming', 'data', 'python', 'code', 'geeks', 'computer', 'engineer', 'word', 'science', 
             'machine', 'java', 'college', 'player', 'mobile', 'image'] 
    word = random.choice(words)                   

    count = 0
    length = len(word)
    display = '*' * length
    alreadyGuessed = []
    playGame = ""


#PythonGeeks: Re-excution of the game when the first round ends:
def play_again():
    global playGame
    playGame = input("Do You want to play again? y = yes, n = no \n")
    while playGame not in ["y", "n","Y","N"]:
        playGame = input("Do You want to play again? y = yes, n = no \n")
    if playGame == "y":
        main()
    elif playGame == "n":
        print("Thanks For Playing!")
        exit()


#PythonGeeks: Initializing all the conditions 
def hangman():
    global count
    global display
    global word
    global alreadyGuessed
    global playGame
    turns = 6
    guess = input("This is the Hangman Word: " + display + "\nEnter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        alreadyGuessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in alreadyGuessed:
        print("Try another letter.\n")

    else:                      
        count += 1
        #when you guess wrong letter you get hang
        if count == 1:
            time.sleep(1)
            
            print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
            print("Wrong guess. " + str(turns - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "  o   |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
            print("Wrong guess. " + str(turns - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "  o   |\n"
                  "  |   |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
           print("Wrong guess. " + str(turns - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "  o   |\n"
                  " /|\  |\n"
                  "      |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
            print("Wrong guess. " + str(turns - count) + " guesses remaining\n")

        elif count == 5:
            time.sleep(1)
            print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "  o   |\n"
                  " /|\  |\n"
                  " /    |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
            print("Wrong guess. " + str(turns - count) + " last guess remaining\n")

        
        elif count == 6:
            time.sleep(1)
            print("H A N G M A N - Python Geeks\n"
                  "  +---+\n"
                  "  |   |\n"
                  "  o   |\n"
                  " /|\  |\n"
                  " / \  |\n"
                  "      |\n"
                  "      |\n"
                  "=========\n")
            print("Wrong guess. You are hanged, Sorry!!!\n")
            print("The word was:",alreadyGuessed,word)
            play_again()

    if word == '_' * length:
        print("Congrats, you guessed the word! YOU WIN!!")
        play_again()

    elif count != turns:
        hangman()

main()

hangman()