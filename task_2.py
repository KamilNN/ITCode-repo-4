class Human:
    def __init__(self, name=None, city=None, year_of_birth=None):
        self.name = name
        self.city = city
        self.year_of_birth = year_of_birth

    def current_age(self):
        return 2024 - self.year_of_birth


person = Human()
person.name = input("Введите Ваше имя: ")
person.city = input("Ваш город проживания: ")
person.year_of_birth = int(input("Год рождения: "))

print("Ваш возраст:", person.current_age())
