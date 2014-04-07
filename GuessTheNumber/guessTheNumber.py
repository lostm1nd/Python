# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

# initialize global variables used in your code
number = 0
guess_range = 100
number_of_guesses = 7

# helper function to start and restart the game
def new_game():
    global number, number_of_guesses
    
    if guess_range == 100:
        print "Starting new game"
        print "Range is [0, 100)"
        number = random.randrange(0, 100)
        number_of_guesses = 7
        print "Allowed guesses: " + str(number_of_guesses)
    else:
        print "Starting new game"
        print "Range is [0, 1000)"
        number = random.randrange(0, 1000)
        number_of_guesses = 10
        print "Allowed guesses: " + str(number_of_guesses)
    print ""

# define event handlers for control panel
def range100():
    global guess_range
    guess_range = 100
    new_game()

def range1000():
    global guess_range
    guess_range = 1000
    new_game()
    
def input_guess(guess):
    global number_of_guesses
    number_of_guesses -= 1
    
    print "Guess was " + guess
    print "Guesses left: " + str(number_of_guesses)
    guess_num = int(guess)
    if guess_num > number:
        print "The secret number is lower!"
    elif guess_num < number:
        print "The secret number is higher!"
    else:
        print "Correct!"
    
    if number_of_guesses == 0:
        print "You loose!"
        print ""
        new_game()
        
    print ""
    
    

    
# create frame
frame = simplegui.create_frame("Guess the number", 300, 300)


# register event handlers for control elements
frame.add_button("Range 0-100", range100, 120)
frame.add_button("Range 0-1000", range1000, 120)
frame.add_input("Guess the number", input_guess, 100)

# call new_game and start frame
new_game()
frame.start()
