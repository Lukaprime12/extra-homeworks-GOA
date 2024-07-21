friends = [("Luka",19),
           ("Mate",18),
           ("Badri",17),
           ("Gio",16),
           ("Goa",21),
           ("john whatt",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)