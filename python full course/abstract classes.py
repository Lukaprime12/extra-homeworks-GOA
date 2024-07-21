from abc import ABC , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class car(vehicle):
    def go(self):
        print('this car is going')
    def stop(self):
        print('this car stopper')

class motorcycle(vehicle):
    pass


vehicle = vehicle()
car = car()
motorcycle = motorcycle()

vehicle.go()
car.go()
motorcycle.go()