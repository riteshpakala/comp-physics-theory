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
breeding = 0;
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
	for k in living_dolphins:
		k.aging()
		for j in living_dolphins:
			pair_up(k,j)
	for j in living_dolphins:
		if (j.age > j.death and j.dead == 0):
			dead_dolphins.append(j)
			j.dead = 1
	for j in living_dolphins:
		if j.dead == 1:
			del j
	
def pair_up(self,partner):
	if self.eligibility(partner) == True:
		self.reproduce()
		partner.reproduce()
		global breeding
		breeding +=1
		if self.sex == 'Male':
			temp = gender()
			randname = random.randint(0,34)
			if temp == 'Male':
				living_dolphins.append(Dolphins(male_names[randname],partner.name, self.name, temp))
			if temp == 'Female':
				living_dolphins.append(Dolphins(female_names[randname],partner.name, self.name, temp))
		if self.sex == 'Female':
			temp = gender()
			randname = random.randint(0,34)
			if temp == 'Male':
				living_dolphins.append(Dolphins(male_names[randname],self.name, partner.name, temp))
			if temp == 'Female':
				living_dolphins.append(Dolphins(female_names[randname],self.name, partner.name, temp))

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
		self.dead = 0

	def aging(self):
		self.age +=1
	def reproduce(self):
		self.since_reproduction +=1
	def eligibility(self, partner):
		if (self.sex != partner.sex and self.age >= 8 and partner.age >=8 and abs(self.age-partner.age) < 10 and self.since_reproduction <= 8 and partner.since_reproduction <= 8 and self.name != partner.name):
			return True
        

name()
'''
for j in xrange(0,len(living_dolphins)):
        if i > living_dolphins[j].death:
            dead_dolphins.append(living_dolphins[j])
'''
#initial 4 dolphins
j = 0;
while(j<2):
	i = random.randint(0,4)
	living_dolphins.append(Dolphins(male_names[i],0,0,'Male'))
	living_dolphins.append(Dolphins(female_names[i],0,0,'Female'))
	j+=1
j=0;

for i in range(0,150):
	advance_year()

	if i == 100:
		print '##################################################'
		print 'Entering year {:g} with {:g} dolphins, with {:g} breeding.'.format(i, len(living_dolphins), breeding)
		print 'at year {:g}, there are {:g} living dolphins.\nthere have been {:g} births total.'.format(i, len(living_dolphins), breeding)
	if (i%25 == 0 or i == 0 or i == 149) and i != 100:
		print '##################################################'
		print 'Entering year {:g} with {:g} dolphins, with {:g} breeding.'.format(i, len(living_dolphins), breeding)