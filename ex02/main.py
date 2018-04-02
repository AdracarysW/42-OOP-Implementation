
from animal import Animal
from cat import Cat
from dog import Dog

if __name__ == '__main__':
    an = Animal()
    do = Dog()
    ca = Cat()
    do.speak()
    ca.speak()
    an.sleep()
    do.sleep()
    ca.sleep()
