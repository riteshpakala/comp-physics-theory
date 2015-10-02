'''
HW04
Ritesh Pakala
Partner: Ian Cone
Creates a class whale with name, sex, and age. 
Creates whales from a list of names, randomly assigning genders.

'''

import datetime
import time
import random

class Whale:
    def __init__(self, name, sex):
        print 'A {:s} whale named {:s} is born'.format(sex, name)
        self.born = datetime.datetime.now()
        self.name = name
        self.sex = sex
        
    def sing(self):
        return '\a \a \a \a \a'
    
    def whale_age(self):
        return datetime.datetime.now() - self.born
    
    def __str__(self):
        return 'A whale named {:s} {:s}'.format(self.name, self.age)
    

whale_names = ['Holden', 'Jake', 'James', 'Johnathan', 'Mary', 'Ritesh',\
               'Joshua', 'Joseph', 'Josef', 'John', 'George', 'Charlotte',\
               'Taylor', 'Spongebob', 'David', 'Joe', 'Tyler', 'Mahesh', 'Kelly',\
              'Paul']

def sex():
    if random.randrange(2) == 0:
        return 'Male'
    else:
        return 'Female'

whale = []
    

    
for i in whale_names:
    whale.append(Whale(i,sex()))
    
print '\nA whale named {:s} (age: {:s})'.format(whale[0].name, whale[0].whale_age()) 
print whale[0].sing()