class Cow:
    can_milk = True


class Horse:
    can_milk = False


class Mule(Cow, Horse):
    can_milk = False


m = Mule()


# print(m.can_milk)


class Form:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return f'{self.a}, {self.b}'


class Square(Form):
    def area(self):
        return self.a * self.b


class Recrangle(Form):
    def area(self):
        return (self.a + self.b) * 2


class Circle(Form):
    pass


square = Square(4, 5)
rectangle = Recrangle(2, 3)
circle = Circle(8, 7)


# print(square.area())
# print(rectangle.area())
# print(circle.area())


class Pizza:
    def __init__(self, size, ingredients):
        self.size = size
        self.ingredients = ingredients


class Margharita(Pizza):
    def __init__(self):
        super().__init__(23, ['tomato', 'oreghano'])


class FourCheese(Pizza):
    def __init__(self):
        super().__init__(23, ['mozzarella', 'cheddar', 'cheese1', 'cheese2'])


pizza = Pizza(25, ['mushrooms', 'chiken'])
margharita = Margharita()
fourcheese = FourCheese()


# print(pizza.ingredients)
# print(margharita.ingredients)
# print(fourcheese.ingredients)


class Car:
    def __init__(self, fuel):
        self.fuel = fuel


class Truck(Car):
    def __init__(self):
        super().__init__('diesel')


class SportCar(Car):
    def __init__(self):
        super().__init__('98 petrol')


class SuperCar(Car):
    def __init__(self):
        super().__init__('100 petrol')


car = Car('92 petrol')
truck = Truck()
sportcar = SportCar()
supercar = SuperCar()

print(truck.fuel)
print(sportcar.fuel)
print(supercar.fuel)
