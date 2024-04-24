class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p-self.a) * (p-self.b) * (p-self.c)) ** 0.5


triangle1 = Triangle(3, 4, 5)
print("Периметр треугольника:", triangle1.perimeter())
print("Площадь треугольника:", triangle1.area())
