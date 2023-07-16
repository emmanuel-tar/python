"""
    Friend Game to guess what Planet I am
"""



#----------------------
# Variable declaration
#----------------------
correct_guess:bool = False
guess:str =''
planet:str = 'Zortan'

#----------------------
# Receiving Input from User
#----------------------

while correct_guess is not True:
    guess = input('Emmanuel Says: Can You Guess My Planet? >>> ')

    if guess.lower() == planet.lower():
        print('Right Guess, Emmanuel is in Zortan')
        correct_guess = True
    else:
        print('Emmanuel Says: Wrong Choice, Try Again!')