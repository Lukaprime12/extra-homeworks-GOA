countries = {'georgia':'Tbilisi',
            'USA':'washington',
            'China':'beijing',
            'india':'new delhi'}
countries.update({'ohio':'Nyc'})
countries.pop('China')
countries.clear()
# print(countries['georgia'])
# print(countries.get('georgia'))
# print(countries.values())
# print(countries.items())

for key,value in countries.items():
    print(key,value)
