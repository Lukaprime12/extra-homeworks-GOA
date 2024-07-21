class car:

    def turn_on(self):
        print('you started the engine')

    def car_self(self):
        print('you drive the car')
    
    def brake(self):
        print('you step on brakes')
    
    def turn_off(self):
        print('you turned the car off')

car = car()

# car.turn_on().drive()
# car.brake().turn_off()
car.turn_on().turn_off().brake().car_self()