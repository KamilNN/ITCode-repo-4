class MixinFood:
    @staticmethod
    def nutrition():
        print("Основное вещество в продукте:")


class Fats:
    @staticmethod
    def print_fats(fats):
        print(f"Жиры: {fats}\n")


class Proteins:
    @staticmethod
    def print_proteins(proteins):
        print(f"Белки: {proteins}\n")


class Carbohydrates:
    @staticmethod
    def print_carbohydrates(carbohydrates):
        print(f"Углеводы: {carbohydrates}\n")


class Sweets(MixinFood, Carbohydrates):
    pass


class HighProtein(MixinFood, Proteins):
    pass


eggs = HighProtein()
eggs.nutrition()
eggs.print_proteins(12)

candy = Sweets()
candy.nutrition()
candy.print_carbohydrates(60)
