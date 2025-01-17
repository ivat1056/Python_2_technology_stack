import random

class Hero:
    def __init__(self, name, role, health, attack):
        self.name = name
        self.role = role
        self.health = health
        self.attack = attack

    def strike(self, opponent):
        """Метод для нанесения удара противнику"""
        damage = random.randint(0, self.attack)
        opponent.health -= damage
        print(f"{self.name} ({self.role}) наносит {damage} урона {opponent.name} ({opponent.role}).")
        if opponent.health <= 0:
            print(f"{opponent.name} ({opponent.role}) побеждён!")

    def is_alive(self):
        """Метод для проверки, жив ли герой"""
        return self.health > 0

    def __str__(self):
        return f"{self.name} ({self.role}) — Здоровье: {self.health}, Атака: {self.attack}"
    
knight = Hero("Ричард", "Рыцарь", 100, 20)
rogue = Hero("Тень", "Разбойник", 80, 25)
print("Начальное состояние персонажей:")
print(knight)
print(rogue)
print()
print("=== Битва начинается! ===")
while knight.is_alive() and rogue.is_alive():
    knight.strike(rogue)
    if rogue.is_alive():
        rogue.strike(knight)
    print(knight)
    print(rogue)
    print()
if knight.is_alive():
    print("Победитель: Ричард (Рыцарь)!")
else:
    print("Победитель: Тень (Разбойник)!")
print()
dragon = Hero("Смертоносец", "Дракон", 150, 30)
print("=== Новая битва: рыцарь против дракона ===")
while knight.is_alive() and dragon.is_alive():
    knight.strike(dragon)
    if dragon.is_alive():
        dragon.strike(knight)
    print(knight)
    print(dragon)
    print()
if knight.is_alive():
    print("Победитель: Ричард (Рыцарь)!")
else:
    print("Победитель: Смертоносец (Дракон)!")
