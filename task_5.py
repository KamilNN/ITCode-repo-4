class Employee:
    def __init__(self, finished_projects):
        self.salary = 20000
        self.finished_projects = finished_projects

    def get_paid(self):
        self.salary += self.finished_projects * 2000
        return self.salary


class Worker(Employee):
    def get_paid(self):
        self.salary += self.finished_projects * 1000
        return self.salary


class Manager(Employee):
    def get_paid(self):
        self.salary += self.finished_projects * 5000
        return self.salary


worker_1 = Worker(10)
manager_1 = Manager(15)
print("Зарплата работника №1:", worker_1.get_paid())
print("Зарплата менеджера №1:", manager_1.get_paid())
