from abc import ABC, abstractmethod

class Ingredient(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity


class Fruit(Ingredient):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name

    def get_quantity(self):
        return self.quantity

print("Задание 1:")
vegetable = Vegetable("Carrot", 10)
fruit = Fruit("Apple", 5)
print(f"Vegetable: {vegetable.get_name()}, Quantity: {vegetable.get_quantity()}")
print(f"Fruit: {fruit.get_name()}, Quantity: {fruit.get_quantity()}")
print()

class Dinosaur(ABC):
    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

class Carnivore(Dinosaur):
    def __init__(self, name, breed, height, weight):
        self.name = name
        self.breed = breed
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Carnivore"

class Herbivore(Dinosaur):
    def __init__(self, name, breed, height, weight):
        self.name = name
        self.breed = breed
        self.height = height
        self.weight = weight

    def get_personal_name(self):
        return self.name

    def get_breed(self):
        return self.breed

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_diet(self):
        return "Herbivore"

class DinosaurPark:
    def __init__(self):
        self.dinosaurs = []

    def add_dinosaur(self, dinosaur):
        self.dinosaurs.append(dinosaur)

    def list_dinosaurs(self):
        return [d.get_personal_name() for d in self.dinosaurs]

    def list_carnivores(self):
        return [d.get_personal_name() for d in self.dinosaurs if d.get_diet() == "Carnivore"]

    def list_herbivores(self):
        return [d.get_personal_name() for d in self.dinosaurs if d.get_diet() == "Herbivore"]

print("Задание 2:")
park = DinosaurPark()
t_rex = Carnivore("Rex", "T-Rex", 12, 8000)
triceratops = Herbivore("Tri", "Triceratops", 10, 6000)
park.add_dinosaur(t_rex)
park.add_dinosaur(triceratops)
print("All dinosaurs:", park.list_dinosaurs())
print("Carnivores:", park.list_carnivores())
print("Herbivores:", park.list_herbivores())
print()

class BankAccount:
    def __init__(self, initial_balance, interest_rate):
        self.__balance = initial_balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"Withdraw: {amount}")
        else:
            print("Insufficient funds")

    def add_interest(self):
        interest = self.__balance * self.__interest_rate
        self.__balance += interest
        self.__transactions.append(f"Interest added: {interest}")

    def history(self):
        return self.__transactions

print("Задание 3:")
account = BankAccount(1000, 0.05)
account.deposit(500)
account.withdraw(300)
account.add_interest()
print("Transaction history:")
for transaction in account.history():
    print(transaction)
print()

class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = 0

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def get_total_salary(self):
        return self.__salary + self.__bonus

print("Задание 4:")
employee = Employee("John Doe", 30, 50000)
employee.set_bonus(10000)
print(f"Employee: {employee.get_name()}, Age: {employee.get_age()}, Total Salary: {employee.get_total_salary()}")
