from datetime import datetime


class Student:
    pass


# class CountryAddress:
# pass

# def sample:
#     pass

student1 = Student()
student2 = Student()

# print(student1)
# print(student2)

student1.name = 'Dima'
student1.email =  'dima@gmail.com'
student1.age = 16

student2.name = 'Emir'
student2.email = 'emir@gmail.com'
student2.age = 12

# print(student1.name, student1.email, student1.age)
# print(student2.name, student2.email, student2.age)

class Employee:
    def __init__(self, name, email, age):
        self.imya = name
        self.email = email
        self.age = age

    def get_info(self,):
        return f'{self.imya}, {self.email}, {self.age}'

    def age_check(self):
        return 'not 18 yet' if self.age < 18 else 'legal to work'

employee1 = Employee('Dima', 'dima@gmail.com', 16)
employee2 = Employee('Emir', 'emir@gmail.com', 13)

# print(employee1)
# print(employee2)

# print(employee1.get_info())
# print(employee2.get_info())
# print(employee1.age_check())
# print(employee2.age_check())

"""
Создать методок класса Employee, который будет проверять возраст объекта.
Если возраст меньше 18 лет, то функция вернет
"Не достигли 18 лет"
"""

class Dog:
    amount_of_legs = 4

    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color
        self.friends = []
    def get_info(self):
        return f'{self.name} {self.breed} {self.color}'

    def bark(self):
        return 'Woof-Woof'

    def eat(self, food):
        return f'Woof {food} if woofy delicious!'

    def make_friend(self, friend):
        self.friend = friend
        friend.friend = self

    def make_more_friends(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

haski = Dog('Hachiko', 'haski', 'gray')
retriever = Dog('Beathoven', 'retriver', 'golden')
alabai = Dog('Max', 'alabai', 'black')

# print(haski.amount_of_legs)
# print(retriever.amount_of_legs)

# print(haski.bark())
# print(haski.eat('bones'))
# print(haski.get_info())
# haski.make_friend(retriever)
# print(haski.friend.name)
# print(retriever.friend.name)
# haski.make_friend(alabai)
# print(haski.make.name)
haski.make_more_friends(alabai)
haski.make_more_friends(retriever)
# print(haski.friends)
#
# for friend in haski.friends:
#     print(friend.name)


class Car:
    brand = 'BMW'
    quantity_of_wheels = 4
    type = 'petrol engine'

    def __init__(self, model, price, year, mileage, color, volume, fuel):
        self.model = model
        self.price = price
        self.year = year
        self.mileage = mileage
        self.color = color
        self.volume = volume
        self.fuel = fuel

    def get_info(self):
        return f'{self.model} {self.price} {self.year} ' \
               f'{self.mileage} {self.color} {self.volume} {self.fuel}'

    def bip(self):
        print('bip-bip!')

    def drive(self):
        if self.fuel < 20:
            return 'Not enough fuel'
        else:
            self.mileage += 100
            self.price -= 100
            self.fuel -= 20




e34 = Car('e34', 3000, '1994', 200000, 'black', 2.494, 32)
e53 = Car('e54', 15000, '2003', 150000, 'grey', 4.6, 26)
e39 = Car('e39', 25000, '2003', 134000, 'grey', 4.9, 30)

# print(e34.get_info())
# e34.bip()
e53.drive()
# print(e39.fuel)


class Student:
    arm = 2
    legs = 2
    nose = 1
    def __init__(self, name, surname, age, phone, lang):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.lang = lang
        self.prog_lang = []


    def get_info(self):
        return f'{self.name}, {self.surname}, {self.age}, ' \
               f'{self.phone}, {self.lang}'


    def method(self, language):
        self.prog_lang.append(language)
        return self.prog_lang

    def programming_way(self):
        if 'python' in self.lang and 'js' in self.lang:
            print('i am fullstack dev')

        elif 'python' in self.lang:
            print('i am backend dev')

        elif 'js' in self.lang:
            print('i am frontend dev')


dima = Student('dima', 'klimenko', 16, '803096', ['ru'])


dima.method('python')
dima.method('js')
print(dima.get_info())
dima.programming_way()


class Home:
    #class veriable
    windows = True
    doors = True

    def __init__(self, area, price, address, year, gas,
                 electicity, sewerage, furniture):
#       instance variables
        self.area = area
        self.price = price
        self.address = address
        self.year = year
        self.gas = gas
        self.electicity = electicity
        self.sewerage = sewerage
        self.furniture = list(furniture)

    def get_info(self):
        return f'{self.area}, {self.price}, {self.address}, ' \
               f'{self.year}, {self.gas}, {self.electicity}' \
               f'{self.sewerage}, {self.furniture}'

    def add_furniture(self, furn):
        if len(self.furniture) * 40 >= self.area:
            print('you cant add more furniture')
        else:
            self.furniture.append(furn)


home1 = Home(100, 20000, 'Bishkek', '2019', 'gas attend', 'electicity attend',
             'sewerage attend', ['chair', 'table'])

# print(home1.get_info())
# home1.add_furniture('bed')
# print(home1.get_info())
# home1.add_furniture('lol')

class User:
    amount_of_accounts = 1
    secondary_education = True

    def __init__(self, username, first_name, second_name,
                 phone_number, email):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone_number
        self.email = email
        self.date_joined = datetime.now()
        self.followers = []
        self.following = []

    def get_info(self):
        return f'{self.username}, {self.first_name}, {self.second_name},' \
               f'{self.phone}, {self.email}, {self.date_joined}'

    def follow(self, user):
        self.followers.append(user)
        user.following.append(self)

    def follow_count(self):
        return len(self.followers), len(self.following)

user1 = User('solarium', 'dima', 'klim', '803096', 'dima@gmail.com')
user2 = User('eigo', 'diman', 'klimenko', '804096', 'diman@gmail.com')
user3 = User('coldbody', 'dimchik', 'klims', '805096', 'dimchik@gmail.com')

user1.follow(user2)
user2.follow(user3)
user3.follow(user1)
user3.follow(user2)

# print([user.username for user in user1.followers])
# print([user.username for user in user2.followers])
# print([user.username for user in user3.followers])
#
# print([user.username for user in user1.following])
# print([user.username for user in user2.following])
# print([user.username for user in user3.following])
#
# print(user1.follow_count())






# def get_info(self):
#     return f'{self.name}, {self.surname}, {self.age}, ' \
#            f'{self.phone}, {self.lang}'







""""
1) Создать класс машины
2) Создать три аттрибута класса машины с общими характеристиками
3) Создать метод конструктор, у которого следующие аргументы:
 - Модель машины
 - Цена
 - Год выпуска
 - Пробег
 - Цвет
 - Объем
 - Остаток бензина
4) Создать метод, который даст всю информацию о машине
5) Создать действие для машины, который будет сигналить
6) Создать метод, который увеличит пробег машины на 100 км.
Тем самым понизит общую стоимость машины на 100$ и
остаток бензина на 20 литров
7) Extra: Если остаток бензина меньше 20 литров,
то мы не сможем проехать 100 км (вызвать метод, созданный на 6 пункте)
"""