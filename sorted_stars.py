from pprint import pprint

data = [
('Alpha Centauri A', 4.3, 0.26, 1.56),
('Alpha Centauri B', 4.3, 0.077, 0.45),
('Alpha Centauri C', 4.2, 0.00001, 0.00006),
("Barnard's Star", 6.0, 0.00004, 0.0005),
('Wolf 359', 7.7, 0.000001, 0.00002),
('BD +36 degrees 2147', 8.2, 0.0003, 0.006),
('Luyten 726-8 A', 8.4, 0.000003, 0.00006),
('Luyten 726-8 B', 8.4, 0.000002, 0.00004),
('Sirius A', 8.6, 1.00, 23.6),
('Sirius B', 8.6, 0.001, 0.003),
('Ross 154', 9.4, 0.00002, 0.0005),
]

def dist_key(item):
    return item[1]

def app_key(item):
    return item[2]

def abs_key(item):
    return item[3]

def distance():
    a = (sorted(data, key = dist_key, reverse = True))
    print '\nRanked by Distance:'
    for i in range(0, len(data)):
        print(a[i][0], a[i][1])
    print '\n'

def apparent():
    b = sorted(data, key = app_key, reverse = True)
    print 'Ranked by Apparent Brightness:'
    for i in range(0, len(data)):
        print(b[i][0], b[i][2])
    print '\n'

def absolute():
    c = sorted(data, key = abs_key, reverse = True)
    print 'Ranked by Absolute Brightness:'
    for i in range(0, len(data)):
        print(c[i][0], c[i][3])
    print '\n'

distance()
apparent()
absolute()