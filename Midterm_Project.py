import datetime as dt
import random
import numpy as np
import pdb as p
import urllib
import re
import matplotlib.pyplot as plt
import networkx as nx

male_names = []
female_names = []
middle_names = []
living_dolphins = []
dead_dolphins = []
dolphins_dict = {}
full_dict = {}
breeding = 0;
main_is_born = 0;
probability = 0;

filename = "male_names.txt" 
with open(filename,"r") as f:
	x = f.read()
	male_name_list = eval(x)
	random.shuffle(male_name_list)
    
            
filename = "female_names.txt"
with open(filename,"r") as f:
	x = f.read()
	female_name_list = eval(x)
	random.shuffle(female_name_list)
	
filename = "middle_names.txt"
with open(filename,"r") as f:
	x = f.read()
	middle_name_list = eval(x)
	random.shuffle(middle_name_list)
    

def gender():
    if random.randint(0,1) == 0:
        return 'Male'
    else:
        return 'Female'

########################################################################################
#only runs first time#as it generates all the names#       
def name():
	boy_names = ''
	girl_names = ''
 	for i in range(1,226):
		url1 = 'http://www.prokerala.com/kids/baby-names/boy/page-'+str(i)+'.html'
		infile1 = urllib.urlopen(url1)      
		lines1 = infile1.readlines()
		infile1.close()
		for line1 in lines1:
			m1 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line1)
			if m1:
				male_names.append(m1.group(2))
		
	for i in range(1,171):	
		url2 = 'http://www.prokerala.com/kids/baby-names/girl/page-'+str(i)+'.html'
		infile2 = urllib.urlopen(url2)
		lines2 = infile2.readlines()
		infile2.close()
		for line2 in lines2:
			m2 = re.search("(nameDetails\">)([A-Z].*[a-z])<", line2)
			if m2:
				female_names.append(m2.group(2))
				
	dir_path = "/Users/Clarke/Documents/USF/Computational\ Physics"
	filenm1 = dir_path + "male_names.txt"                
	with open(filenm1,"w") as f:
		f.write(str(male_names)) 
	filenm2 = dir_path + "female_names.txt"                
	with open(filenm2,"w") as f:
		f.write(str(female_names)) 
	filenm2 = dir_path + "middle_names.txt"                
	with open(filenm2,"w") as f:
		f.write(str(female_names)) 
########################################################################################
########################################################################################


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
		global main_is_born
		global my_dolphin
		breeding +=1
		temp = gender()
		global probability
		
		if temp == 'Male':
			try:
				name = male_names.next()
			except StopIteration:
				name = middle_names.next()
		else:
			try:
				name = female_names.next()
			except StopIteration:
				name = middle_names.next()
		
		if self.sex == 'Male':
				probability += 1
				living_dolphins.append(Dolphins(name,partner.name, self.name, temp))
		else:
				living_dolphins.append(Dolphins(name,self.name, partner.name, temp))
				
		if main_is_born == 1:
			my_dolphin = living_dolphins[len(living_dolphins)-1]
			main_is_born = 0

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
		self.since_reproduction +=1
	def reproduce(self):
		self.since_reproduction = 0
	def eligibility(self, partner):
		if (self.sex != partner.sex\
		and self.mother != partner.mother\
		and self.father != partner.father\
		and self.age >= 8 and partner.age >=8\
		and abs(self.age-partner.age) < 10\
		and self.since_reproduction >= 8\
		and partner.since_reproduction >= 8\
		and self.name != partner.name\
        and (self.mother != partner.mother or self.father != partner.father)):
			return True
        
def make_name(sex):
	if sex == 'Male':
		for i in range(0, len(male_name_list)):
			yield male_name_list[i]
			i +=1

	if sex == 'Female':
		for i in range(0, len(female_name_list)):
			yield female_name_list[i]
			i +=1
	
	if sex == 'Middle':
		for i in range(0, len(middle_name_list)):
			yield middle_name_list[i]
			i +=1

if(male_name_list>0):
	male_names = make_name('Male')
	female_names = make_name('Female')
	middle_names = make_name('Middle')
else:
	name()


init_dolphins_25 = 0
init_dolphins_50 = 0
init_dolphins_75 = 0
init_dolphins_100 = 0
init_dolphins_125 = 0
init_dolphins_150 = 0
last_dolphins_25 = 0
last_dolphins_50 = 0
last_dolphins_75 = 0
last_dolphins_100 = 0
last_dolphins_125 = 0
last_dolphins_150 = 0
total_dolphins_25 = 0
total_dolphins_50 = 0
total_dolphins_75 = 0
total_dolphins_100 = 0
total_dolphins_125 = 0
total_dolphins_150 = 0
my_dolphin = Dolphins('Ritesh','god', 'god2', 'male')#Just initializing the main dolphin
def run_all_trials(n):
	for k in range (1,n+1):
		global init_dolphins_25
		global init_dolphins_50
		global init_dolphins_75
		global init_dolphins_100
		global init_dolphins_125
		global init_dolphins_150
		global last_dolphins_25
		global last_dolphins_50
		global last_dolphins_75
		global last_dolphins_100
		global last_dolphins_125
		global last_dolphins_150
		global total_dolphins_25
		global total_dolphins_50
		global total_dolphins_75
		global total_dolphins_100
		global total_dolphins_125
		global total_dolphins_150
		
		print 'Trial No. {:g}'.format(k)
		full_dict[k] = dolphins_dict
		global year
		year = 0
		global breeding
		breeding = 0
		global total_dolphins
		global living_dolphins
		global main_is_born
		living_dolphins = []
		dead_dolphins = []
	
		
		for na1 in {'John', 'James'} :
			living_dolphins.append(Dolphins(na1,'god','god2','Male'))
		for na2 in {'Rebecca', 'Jenny'} :
			living_dolphins.append(Dolphins(na2,'god4','god3','Female'))
		
		for i in range(0,150):
			advance_year()
			if i == 70:
				main_is_born = 1
			if i == 100:
				print '##################################################'
				print 'Entering year {:g} with {:g} dolphins, with {:g} breeding.'.format(i, len(living_dolphins), breeding)
				print 'at year {:g}, there are {:g} living dolphins.\nthere have been {:g} births total.'.format(i, len(living_dolphins), breeding)
				total_dolphins_100 += len(living_dolphins)
				if(k==1):
					init_dolphins_100 += len(living_dolphins)
				if(k==n):
					last_dolphins_100 += len(living_dolphins)
			if (i%25 == 0 or i == 0 or i == 149) and i != 100:
				print '##################################################'
				print 'Entering year {:g} with {:g} dolphins, with {:g} breeding.'.format(i, len(living_dolphins), breeding)
				if(i==25): 
					total_dolphins_25 += len(living_dolphins)
					if(k==1):
						init_dolphins_25 += len(living_dolphins)
					if(k==n):
						last_dolphins_25 += len(living_dolphins)
				if(i==50): 
					total_dolphins_50 += len(living_dolphins)
					if(k==1):
						init_dolphins_50 += len(living_dolphins)
					if(k==n):
						last_dolphins_50 += len(living_dolphins)
				if(i==75): 
					total_dolphins_50 += len(living_dolphins)
					if(k==1):
						init_dolphins_75 += len(living_dolphins)
					if(k==n):
						last_dolphins_75 += len(living_dolphins)
				if(i==125): 
					total_dolphins_125 += len(living_dolphins)
					if(k==1):
						init_dolphins_125 += len(living_dolphins)
					if(k==n):
						last_dolphins_125 += len(living_dolphins)
				if(i==149): 
					total_dolphins_150 += len(living_dolphins)
					if(k==1):
						init_dolphins_150 += len(living_dolphins)
					if(k==n):
						last_dolphins_150 += len(living_dolphins)
		print '\n'
		
	########################################################################################
	#Graph
	fig = plt.figure()
	ax = plt.subplot(111)
	
	total_dolphins_25 /= n
	total_dolphins_50 /= n
	total_dolphins_75 /= n
	total_dolphins_100 /= n
	total_dolphins_125 /= n
	total_dolphins_150 /= n
	init_population = [0, init_dolphins_25, init_dolphins_50, init_dolphins_75, init_dolphins_100, init_dolphins_125, init_dolphins_150]
	population = [0, total_dolphins_25, total_dolphins_50, total_dolphins_75, total_dolphins_100, total_dolphins_125, total_dolphins_150]
	last_population = [0, last_dolphins_25, last_dolphins_50, last_dolphins_75, last_dolphins_100, last_dolphins_125, last_dolphins_150]
	years = [0, 25, 50, 75, 100, 125, 150]
	x = np.linspace(0,150,10000)
	plt.plot(years, init_population, color='red')
	plt.plot(years, population, color='blue')
	plt.plot(years, last_population, color='red')
	plt.fill_between(years, init_population, last_population, color='red')
	
	
	plt.savefig('population_growth.pdf')
	########################################################################################
	########################################################################################
		
		
	########################################################################################
	#Genealogy graph and output
	if(k==n):
		print my_dolphin.name
		mother = my_dolphin.mother
		father = my_dolphin.father
		cousins = []
		siblings = []
	
		for tracker in living_dolphins:
			if tracker.mother == my_dolphin.mother and tracker.father == my_dolphin.father:
				siblings.append(tracker)
			elif tracker.mother == my_dolphin.mother or tracker.father == my_dolphin.father:
				cousins.append(tracker)
		
		fig = plt.figure()
		ax = plt.subplot(111)
		
		G = nx.Graph()

		G.add_node(my_dolphin.name)#, pos=(1,1))
		G.add_node(my_dolphin.mother)
		G.add_node(my_dolphin.father)
		G.add_edge(my_dolphin.name, my_dolphin.mother, weight=30)
		G.add_edge(my_dolphin.name, my_dolphin.father, weight=30)
		
		print '--Siblings:\n'		
		for sibling in siblings:
			G.add_node(sibling.name)
			G.add_edge(my_dolphin.mother, sibling.name, weight=5)
			G.add_edge(my_dolphin.father, sibling.name, weight=5)
			print '{:s}'.format(sibling.name)
		print '--Cousins:\n'	
		for cousin in cousins:
			G.add_node(cousin.name)
			if cousin.father == my_dolphin.father:
				G.add_edge(my_dolphin.father, cousin.name, weight=1)
			else:
				G.add_edge(my_dolphin.mother, cousin.name, weight=1)
			print '{:s}'.format(cousin.name)
		pos=nx.spring_layout(G, scale=2)
		nx.draw_networkx(G, pos)
		plt.savefig('genealogy.pdf')
	########################################################################################
	print "\nProbability rate: {:f}%".format(((probability*1.)/total_dolphins_150)*100)
	########################################################################################
	#Prints Plot and Genealogy Tree after Terminal displays relative information
	plt.show()
	########################################################################################
	########################################################################################
	
run_all_trials(10)