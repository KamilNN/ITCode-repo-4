class Calculator:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def substraction(a, b):
        return a - b

    @staticmethod
    def division(a, b):
        return a / b


print("Сложение", Calculator.addition(3, 4))
print("Вычитание", Calculator.substraction(3, 4))
print("Умножение", Calculator.multiplication(3, 4))
print("Деление", Calculator.division(3, 4))
