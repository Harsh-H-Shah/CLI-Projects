from random import random
import string
import random
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''
def hint(secret_word, letters_guessed):
    s=''
    for i in secret_word:
        if i not in letters_guessed:
            s+=i
    c = random.choice(s)
    letters_guessed.append(c)
    return ("Hint : " + c)

def get_images(lives):
    return IMAGES[8-lives]

def isvalid(s, letters_guessed):
    if len(s) != 1:
        return False
    elif ord(s)<65 and ord(s)>90 or ord(s)<97 and ord(s)>122 and s in letters_guessed:
        return False
    return True

def is_word_guessed(secret_word, letters_guessed):

    for s in secret_word:
        if s not in letters_guessed:
            return False
    return True
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the word correctly )
      return False (wrong selection)
    '''

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    string = ""
    for i in range(26):
        if chr(i+97) not in letters_guessed:
            string+=chr(i+97)
    # letters_left = string.ascii_lowercase
    # return letters_left
    return string

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    lives = 8
    num_of_hints = 1
    letters_guessed = []

    while lives>0:

        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if guess.lower()=="quit":
            break
        elif guess.lower()=="hint":
            if num_of_hints==1:
                print("Are you sure? You can use hint only once. y/n: ")
                decision = input()
                if decision.lower()=="y":
                    num_of_hints = 0
                    print(hint(secret_word, letters_guessed))
                    continue
                elif decision.lower()=="n":
                    continue
                else:
                    print("Please provide a valid input: ")
                    continue
            else:
                print("Sorry you have used your hint already")
                continue

        elif isvalid(letter, letters_guessed):

            if letter in secret_word:
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                if is_word_guessed(secret_word, letters_guessed):
                    print(" * * Congratulations, you won! * * ", end='\n\n')
                    break
            else:
                print("Oops! That letter is not in my word: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                print("\t\t\tYou have " + str(lives-1) + " lives left")
                print(get_images(lives))
                lives-=1
                letters_guessed.append(letter)
                print("")
        else:
            print("Kindly provide a valid input: ")
            continue
    
    print("You lose, the word was : " + secret_word)


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
