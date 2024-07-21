class Animal:
    alive = True

    def slumber(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run():
        print('This rabbit is running')

class Fish(Animal):
    def swim(self):
        print('this fish is swimming')

class Hawk(Animal):
    def fly(self):
        print('this hawk is flying')

rabbit_instance = Rabbit()
fish_instance = Fish()
hawk_instance = Hawk()

# print(rabbit_instance.alive)
# fish_instance.eat()
# hawk_instance.sleep()

rabbit_instance.run
fish_instance.swim
hawk_instance.fly