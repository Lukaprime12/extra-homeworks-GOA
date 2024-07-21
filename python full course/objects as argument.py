class car:

    color = None

class motorcycle:

    color: None


def change_color(vehicle,color):
    vehicle.color = color


car_1 = car()
car_2 = car()
car_3 = car()

bike_1 = motorcycle()

change_color(car_1,'red')
change_color(car_2,'white')
change_color(car_3,'blue')
change_color(car_1,'black')

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(car_1.color)