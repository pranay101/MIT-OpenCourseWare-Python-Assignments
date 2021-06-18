# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import msvcrt
from os import system
import string

WORDLIST_FILENAME = "words.txt"


#helpers function
# Python program to convert a list to string
    
# Function to convert  
def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    # return string  
    return str1


def print_format(string_to_print,number_of_guess):
  print("\n\n")
  print("\t" + string_to_print)
  print("\n")
  print("\tNumber of gueses left: ",number_of_guess)
  print("\n\n")


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_list = list(secret_word)
    guessed_word_temp = ""
    for word in secret_word_list:
      if word in letters_guessed:
        guessed_word_temp += word
      else:
        guessed_word_temp += "_"

    # print(guessed_word_temp)
    # print(secret_word)

    return guessed_word_temp == secret_word
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
  
    secret_word_list = list(secret_word)
    guessed_word_temp = ""
    for word in secret_word_list:
      if word in letters_guessed:
        guessed_word_temp += word + " "
      else:
        guessed_word_temp += "_ "

    return guessed_word_temp   



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    string_to_return = ''
    Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for word in Alphabet :
      if word not in letters_guessed:
        string_to_return += word
     
    return string_to_return



    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    print("""
Welcome to hangman.

Rules:
1. In this game computer will generate a word and print it without some of it's letters 
2. Your got to guess the remaining letters.
3. Your are given 6 guesses to get it right.
4. if you guess a vowel and it isn't the part of word, you loose 2 guess
  """)
    Vowel = ['a','e','i','o','u']
    Warning = 3
    # Vowel = 'aeiou'
    number_of_guess = 6
    print(secret_word)
    letters_guessed = []
    trys = 0

    length_of_word = len(secret_word)
    print("I am thinking of a word that is " + str(length_of_word) +" letters long. ")
    print("------------------------------------\n")
    while True:
      if Warning != 3:
        print("\nYou have "+ str(Warning)+" Warnings left.")
      print("You have "+ str(number_of_guess)+" guesses left.")
      print("Available letters: "+ get_available_letters(letters_guessed))

      if number_of_guess <= 0:
        print("Sorry you ran out of guesses!!")
        print("\nThe word is :",secret_word)
        break
      if Warning <= 0:
        print("You've crossed all warning, you are dismissed !!")
        print("------------------------------------\n")
        break

      guessed_letter = str(input("Guess a letter : ")).lower()
      letters_guessed.append(guessed_letter)
      string_to_print = get_guessed_word(secret_word,letters_guessed)

      if guessed_letter == " ":
        print("space is not counted")
        print_format(string_to_print,number_of_guess)

      if guessed_letter in secret_word:
        print("Good guess: "+string_to_print)
        print("------------------------------------\n")
        if is_word_guessed(secret_word,letters_guessed):
          print("Congratulations, you won!")
          print("Your total score for this game is: "+ str(number_of_guess))
           
          print("\nThe word is :" + secret_word)
          break
      else:
        if not guessed_letter.isalpha():
          Warning = Warning-1
          print("You can enter only alphabets !!")
          print("------------------------------------\n")
        else:
          if guessed_letter in Vowel:
            print("You've guessed a vowel so -2")
            print("------------------------------------\n")
            number_of_guess = number_of_guess-2
          else :
            number_of_guess = number_of_guess -1
            print("Oops! That letter is not in my word: " + string_to_print)
            print("------------------------------------\n")

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
