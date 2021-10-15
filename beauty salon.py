import random



class Human:
    def __init__(self, name, sex, year_of_birth, hair_length, nail_length, nail_color = "бесцветные"):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color

    def __str__(self):
        return f'Меня зовут {self.name} , я обладатель длины волос {self.hair_length} и {self.nail_color} ногтей {self.nail_length}'


class Worker:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth


class Manicurist(Worker):
    def do_job(self, other):
        if other.nail_length > 1:
            other.nail_length -= 1
        other.nail_color = random.choice(['красные' , 'фиолетовые' , 'зелёные'])

class Hairdresser(Worker):
    def do_job(self, other):
        if other.hair_length > 1:
            other.hair_length -= 1


class Barber(Worker):
    def do_job(self, other):
        if other.sex == "M":
            if other.hair_length > 1:
                other.hair_length -= 1
        else: 
            raise ValueError


neo = Human( = "Neo", sex = "M", year_of_birth = 1964, hair_length = 10, nail_length = 2)
trinity = Human(name = "Trinity", sex = "F", year_of_birth = 1967, hair_length = 30, nail_length = 5)

manicurist = Manicurist(name = "Samara", sex = "F", year_of_birth = 1992)
hairdresser = Hairdresser(name = "Rosa", sex = "F", year_of_birth = 1985)
barber = Barber(name = "Bob", sex = "M", year_of_birth = 1987)

manicurist.do_job(trinity)
barber.do_job(neo)

print(neo)
print(trinity)