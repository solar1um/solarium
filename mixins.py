class A:
    x = 5

class B:
    x = 10

class C(A,B):
    pass

#Method Resolution Order (MRO)
#Порядок разрешения методов

c = C()
# print(c.x)


class Donkey:
    is_donkey = True


class Horse:
    is_horse = True


class Mule(Donkey, Horse):
    pass


mule = Mule()
# print(mule.is_horse)
# print(mule.is_donkey)


class Transport:
    def drive(self):
        print('driving')

    def carry_goods(self):
        print('carrying goods')

class Car(Transport):
    def carry_passengers(self):
        print('carrying passengers')


class CraneMixin:
    def lift(self):
        print('lifting something')


class TruckWithCrane(Transport, CraneMixin):
    def carry_things(self):
        print('carrying things')


class MotorBoatWithCrane(Transport, CraneMixin):
    def dock(self):
        print('docked')




class Animal:
    def __init__(self, name):
        self.name = name

    def eat_grass(self):
        print('Eating grass')

class MilkOutMixin:
    def milking(self):
        print('Getting milk')

class Cow(Animal, MilkOutMixin):
    pass

class Goat(Animal, MilkOutMixin):
    pass

cow = Cow('cow')
goat = Goat('kozel')

# cow.milking()
# goat.milking()


class PhoneMixin:
    def call(self):
        print('calling...')

class Technology:
    def charge(self):
        print('chargering...')


class MobilePhone(Technology, PhoneMixin):
    def play(self):
        print('playing minecraft')


class HomePhone(Technology, PhoneMixin):
    def funny_song(self):
        print('funny song now playing')

class Computer(Technology):
    def code(self):
        print('coding now!')



