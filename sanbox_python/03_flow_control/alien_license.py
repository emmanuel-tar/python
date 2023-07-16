"""
    Emmanuel want to drive a car and
    he heard that in planet Zortan, There is no age Limit
    for getting a License
"""

#----------------------
# Variable declaration
#----------------------
age: int = 13
planet:str = 'Earth'

#----------------------
# And / Or Statement
#----------------------

planet = 'Zortan'
if age < 16 and planet == 'Earth':
    print('You are not Eligible for a License on Earth')
elif age >16 and planet == 'Earth':
    print('You can apply for a license on Earth')
elif age < 16 or planet == 'Zortan':
    print('You are Eligible for a License on Zortan')