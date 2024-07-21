class duck:

    def walk(self):
        print('This duck is walking')
    
    def talk(self):
        print('This duck is talking')

class chicken:

    def walk(self):
        print('This chicken is walking')
    
    def talk(self):
        print('this chicken is talking')

class person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('you caught the critter!')

duck = duck()
chicken = chicken()
person = person()

person.catch(duck)