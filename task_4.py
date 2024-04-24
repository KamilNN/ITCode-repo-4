class Car:

    def __init__(self, weight, color):
        self.color = color
        self.weight = weight

    def __str__(self):
        return f"\nВес машины: {self.weight}\nЦвет машины: {self.color}\n"


car_1 = Car(2000, 'red')
car_2 = Car(4000, 'green')
print(car_1, car_2)
