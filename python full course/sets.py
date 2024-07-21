utensils = {'fork','spoon','knife','knife','knife','knife'}
# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
dishes = {'bowl','plate','cup','knife'}
# utensils.update(dishes)
dinner = dishes.union(utensils)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))
for x in dinner:
    print(x)