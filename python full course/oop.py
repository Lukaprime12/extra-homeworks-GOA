from car import car

car_1 =car('Chevy','convette',2021,'blue')
car_2 =car('ford','mustang',2022,'red')

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()