import random

class Hero:
    def __init__(self, name, health, armor, power):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.new = True

    def print_info(self):
        print(f"{self.name}: Health = {self.health}, Armor = {self.armor}")
        
    def check_alive(self):
        return self.health > 0
    
    def strike(self, enemy):
        if enemy.armor > 0:
            print(f"{self.name} breaks {enemy.name}'s armor!")
            enemy.armor = 0
        else:
            damage = self.power
            enemy.health -= damage
            print(f"{self.name} hits {enemy.name} for {damage} damage!")
        if not enemy.check_alive():
            print(f"{enemy.name} has been defeated!")

class Warrior(Hero):
    def hello(self):
        if self.new:
            print(f"{self.name} the Warrior enters the battle!")
            self.new = False
        else:
            print(f"{self.name} is ready for another fight!")

    def attack(self, enemy):
        print(f"{self.name} swings a sword at {enemy.name}!")
        self.strike(enemy)

class Dragon(Hero):
    def hello(self):
        if self.new:
            print(f"{self.name} the Dragon roars and joins the fray!")
            self.new = False
        else:
            print(f"{self.name} is back for revenge!")

    def attack(self, enemy):
        print(f"{self.name} breathes fire at {enemy.name}!")
        self.strike(enemy)

def game_cycle():
    print("\n=== Задача 3: Игровой цикл ===")
    knight = Warrior("Sir Lancelot", 100, 50, 20)
    enemies = [
        Hero("Peter the Bandit", 50, 20, 10),
        Hero("Sergey the Bandit", 60, 15, 12),
        Dragon("Drogo", 80, 30, 25),
        Dragon("Vizerion", 90, 40, 30)
    ]
    random.shuffle(enemies)
    for enemy in enemies:
        if not knight.check_alive():
            print("The knight has fallen. The quest ends.")
            break
        print("\nA new enemy appears!")
        enemy.hello()
        knight.hello()
        while knight.check_alive() and enemy.check_alive():
            attacker = random.choice([knight, enemy])
            if attacker == knight:
                knight.attack(enemy)
            else:
                enemy.attack(knight)
        print("Battle ends. Current status:")
        knight.print_info()
    if knight.check_alive():
        print("\nThe knight has defeated all enemies and completed the quest!")
    else:
        print("\nThe knight's journey ends in failure.")

if __name__ == "__main__":
    print("\n=== Задача 1: Суперкласс Hero ===")
    hero_example = Hero("Example Hero", 100, 50, 20)
    hero_example.print_info()
    print("\n=== Задача 2: Классы-наследники Warrior и Dragon ===")
    warrior_example = Warrior("Example Warrior", 100, 50, 30)
    dragon_example = Dragon("Example Dragon", 150, 60, 40)
    warrior_example.hello()
    dragon_example.hello()
    print("\nНачало игрового цикла...")
    game_cycle()
