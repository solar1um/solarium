from datetime import datetime



class Animal:
    amount_of_legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self, food):
        return f'I am eating {food}'

a1 = Animal('animal1', 'white')
a2 = Animal('animal1', 'black')


class Dog(Animal):
    follow_commands = True

    def bark(self):
        return 'Woof!'



class Cat(Animal):
    follow_commands = False

    def meow(self):
        return 'Meow'

c1 =  Cat('cat1', 'red')
# print(c1.name, c1.amount_of_legs)
d1 = Dog('dog1', 'black')
# print(d1.name, d1.amount_of_legs)
# print(d1.eat('bones'))
# print(c1.eat('fish'))

# print(d1.follow_commands)
# print(c1.follow_commands)
#
# print(d1.bark())
# print(c1.meow())




class Person:
    amount_of_arms = 2
    amount_of_legs = 2
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class Teacher(Person):
    teach_people = True

    def reading(self, book):
       return f'now i am reading the {book}!'

class Doctor(Person):
    teach_people = False

    def save_lives(self, live):
        return f"i've saved {live}"

class Banker(Person):
    teach_people = False

    def gun(self, gun):
        return f"now i got a {gun}"

p1 = Teacher('dima', 'klimenko', 16)
p2 = Doctor('dim', 'klime', 17)
p3 = Banker('dimchik', 'klimechick', 18)

# print(p1.reading('capital'))
# print(p2.save_lives('dima'))
# print(p3.gun('desert eagle'))

class Form:

    def set_values(self, height, width):
        self.height = height
        self.width = width


class Square(Form):
    def area(self):
        return self.height * self.width


class Triangle(Form):
    def area(self):
        return (self.height * self.width) / 2


square = Square()
triangle = Triangle()

square.set_values(5, 6)
triangle.set_values(8, 2)

# print(square.area())
# print(triangle.area())


class Human:
    def __init__(self, name, age, phone, address,):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address

    def sleep(self):
        return 'i am sleeping'

class Developer(Human):
    def code(self):
        return 'i am coding'

class BackendDeveloper(Developer):
    def create_apis(self):
        return 'API created'

class PythonDeveloper(BackendDeveloper):
    def develop_with_django(self):
        return 'django used for backend'


class PHPDeveloper(BackendDeveloper):
    def develop_with_laravel(self):
        return 'laravel used for backed'


class FrontendDeveloper(Developer):
    def code_html(self):
        return 'html is done'


python_dev = PythonDeveloper('Pythonist', 25, '996555800800', 'bishkek')
php_dev = PHPDeveloper('PHPist', 23, '+996555100100', 'Karaganda')
js_dev = FrontendDeveloper('Frontend', 20, '+996555200200', 'Tokmok')

# print(python_dev.develop_with_django())
# print(python_dev.create_apis())
# print(python_dev.code())
# print(python_dev.sleep())
#
# print(php_dev.develop_with_laravel())
# print(php_dev.create_apis())
# print(php_dev.code())
#
# print(js_dev.code_html())
# print(js_dev.code())

class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.date_joined = datetime.now()

    def sleep(self):
        return 'now i sleeping'

class RegisteredUser(User):
    registered = True

    def get_date_joined(self):
        return self.date_joined


class ActiveUser(RegisteredUser):
    amount_of_posts = 0

    def add_post(self):
        self.amount_of_posts += 1
        return self.amount_of_posts


dima = ActiveUser('dima', 'klimenko', 16)
dima1 = RegisteredUser('dima', 'klimenko', 16)

# print(dima.sleep())
# print(dima1.get_date_joined())
# print(dima.add_post())
# print(dima.add_post())

class Employee:
    def __init__(self, name, email, age):
        self.imya = name
        self.email = email
        self.age = age
        self.recipe = []

    def get_info(self,):
        return f'{self.imya}, {self.email}, {self.age}'

    def age_check(self):
        return 'not 18 yet' if self.age < 18 else 'legal to work'


employee1 = Employee('Dima', 'dima@gmail.com', 16)
employee2 = Employee('Emir', 'emir@gmail.com', 13)


class Writer(Employee):
    dishes_served = 0
    zp = 0

    def serve_dish(self):
        self.dishes_served += 5
        if self.dishes_served >= 10:
            self.zp += 100
            self.dishes_served = self.dishes_served - 10


dima = Writer('dima', '@mail.ru', 16)
dima2 = Writer('dima', '@mail.ru', 16)
dima.serve_dish()
dima.serve_dish()
dima.serve_dish()
dima.serve_dish()
# print(dima.zp)
# print(dima.zp)
# print(dima.dishes_served)



class Cook(Employee):
    junior_cook = False
    middle_cook = False
    senior_cook = False
    chief = False

    def learn_new_recipe(self, dish):
        self.recipe.append(dish)

        zp = 0
        if len(self.recipe) >= 10:
            self.chief = True
            self.senior_cook = False
            self.middle_cook = False
            self.junior_cook = False
            zp += 1000
        elif len(self.recipe) <= 7 and len(self.recipe) > 5:
            self.senior_cook = True
            self.middle_cook = False
            self.junior_cook = False
            zp += 600
        elif len(self.recipe) <=5 and len(self.recipe) > 3:
            self.middle_cook = True
            self.junior_cook = False
            zp += 400
        elif len(self.recipe) == 3:
            zp += 200
            self.junior_cook = True

        return self.recipe


klim = Cook('name', '@', 16)
klim1 = Cook('name', '@', 16)
# klim2 = Cook('name', '@', 16)

klim.learn_new_recipe('spaghetti')
klim.learn_new_recipe('meth')
klim.learn_new_recipe('plov')
klim.learn_new_recipe('burger')
klim.learn_new_recipe('pizza')
klim.learn_new_recipe('roll')
klim.learn_new_recipe('grechka')
klim.learn_new_recipe('ogurec')
klim.learn_new_recipe('beer')
klim.learn_new_recipe('doshirak')

print(klim.junior_cook)
print(klim.middle_cook)
print(klim.senior_cook)
print(klim.chief)
print(klim.recipe)

# print(klim1.recipe)
