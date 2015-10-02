'''
HW04
Ritesh Pakala
Partner: Ian Cone
Prints out a flight schedule, first by flight, and then by time
'''

airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", \
            "LHR": "London-Heathrow", "SVO": "Moscow", \
            "CDA": "Chicago-Midway", "SBA": "Santa Barbara", \
            "LAX": "Los Angeles","JFK": "New York City", \
            "MIA": "Miami", "AUM": "Austin, Minnesota"}

# airline, number, heading to, gate, time (decimal hours)
flights = [("Southwest",145,"DCA",1,6.00),\
           ("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
           ("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60),\
           ("United",46,"LAX",5,6.5), ("Southwest",23,"SBA",6,12.5),\
           ("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
           ("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),\
           ("United",2032,"MIA",21,15.1),("SpamAir",1,"AUM",42,14.4)]

def getkey(item):
    return item[4]

def schedule(airport_dict,flight_list):
    print 'Flight \t  \t Destination \t      Gate \t  \t Time'
    print '---------------------------------------------------------------'
    for i in range(0,len(flights)):
        print '{:s} {:g} \t {:20s} {:g} \t  \t {:g}'.format(sorted(flights)[i][0],\
                                                             sorted(flights)[i][1],\
                                                             airports[sorted(flights)[i][2]],\
                                                             sorted(flights)[i][3],\
                                                             sorted(flights)[i][4])
    
    

def time(airport_dict,flight_list):
    print 'Flight \t  \t Destination \t      Gate \t  \t Time'
    print '---------------------------------------------------------------'
    for i in range(0,len(flights)):
        print '{:s} {:g} \t {:20s} {:g} \t  \t {:g}'.format(sorted(flights, key = getkey)[i][0],\
                                                             sorted(flights, key = getkey)[i][1],\
                                                             airports[sorted(flights, key = getkey)[i][2]],\
                                                             sorted(flights, key = getkey)[i][3],\
                                                             sorted(flights, key = getkey)[i][4])
        
schedule(airports,flights)
print 
time(airports,flights)
    