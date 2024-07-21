name = 'Luka Codes'
first_name = name[0:4]#[:4]
last_name = name[5:]#[:10]
funky_name = name[0:10:2]
reversed_name = name[::-1]

print(first_name, last_name, funky_name, reversed_name)
website = 'http://google.com'
slice = slice(7, -4)
print(website[slice])