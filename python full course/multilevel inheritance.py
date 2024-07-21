class organism:

    alive = True

    def eat(self):
        print('This animal is eating !')

class Animal(organism):

    
    def slumber(self):
        print('This animal is sleeping !')


class dog(Animal):
    
    def bark(self):
        print('This dog is barking !')


dog = dog
print(dog.alive)
dog.eat()
dog.bark()