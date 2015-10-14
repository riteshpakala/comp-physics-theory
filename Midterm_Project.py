import datetime as dt
import random
import numpy as np
import pdb as p
import urllib
import re

male_names = []
female_names = []
living_dolphins = []
dead_dolphins = []
        
def gender():
    if random.randint(0,2) == 0:
        return 'Male'
    else:
        return 'Female'
        
def name():
	count = 1
 	while count < 2:
		url1 = 'http://www.prokerala.com/kids/baby-names/boy/page-'+str(count)+'.html'
		url2 = 'http://www.prokerala.com/kids/baby-names/girl/page-'+str(count)+'.html'
		infile1 = urllib.urlopen(url1)      
		lines1 = infile1.readlines()
		infile1.close()

		infile2 = urllib.urlopen(url2)      
		lines2 = infile2.readlines()
		infile2.close()

		for line1 in lines1:
			m1 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line1)
			if m1:
				male_names.append(m1.group(2))

		for line2 in lines2:
			m2 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line2)
			if m2:
				female_names.append(m2.group(2))
		count += 1

def advance_year():
    for i in living_dolphins:
        i.aging() 
       
class Dolphins:
    def __init__(self, name, mother, father, sex = gender()):
        self.name = name
        self.sex = sex
        self.age = 0
        self.mother = mother
        self.father = father
        self.death = random.gauss(mu = 35, sigma = 5)
        self.active = 0
        self.since_reproduction = 0

    def aging(self):
        self.age +=1
        self.since_reproduction +=1
    def reproduce(self):
        self.since_reproduction = 0
    def eligibiliy(self, partner):
        if (self.age >= 8 and self.active == 0\
        and partner.age >=8 and partner.active == 0\
        and abs(self.age-partner.age) < 10\
        and (self.mother != partner.mother or self.father != partner.father)):
        	return true

name()
for i in male_names:
    living_dolphins.append(Dolphins(i,0,0,'Male'))
for i in female_names:
    living_dolphins.append(Dolphins(i,0,0,'Female'))

for i in range(0,12):
    advance_year()
    for j in xrange(0,len(living_dolphins)):
        if i> living_dolphins[j].death:
            dead_dolphins.append(living_dolphins[j])
            print living_dolphins[j].name,'has died!'
        print living_dolphins[j].name,'is',living_dolphins[j].age,'years old'