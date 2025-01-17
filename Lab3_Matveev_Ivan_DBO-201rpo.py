import random

class Ghost:
    def __init__(self, nickname, color, feature, speed):
        self.nickname = nickname
        self.color = color
        self.feature = feature
        self.speed = speed

    def print_info(self):
        print(f"Ник: {self.nickname}")
        print(f"Цвет персонажа: {self.color}")
        print(f"Стратегия, которой придерживается персонаж: {self.feature}")
        print(f"Скорость движения: {self.speed}")

    def print_string(self):
        print(f"Призрак {self.nickname} ({self.color}) появился и движется со скоростью {self.speed}.")

class PacMan:
    def __init__(self):
        self.points = 0
        self.lives = 5

    def eat_points(self):
        points = random.randint(20, 50)
        self.points += points
        print(f"Pac-Man съел точки, заработав {points} очков. Всего очков: {self.points}.")

    def move(self):
        directions = ["вверх", "вниз", "влево", "вправо"]
        direction = random.choice(directions)
        print(f"Pac-Man движется {direction}.")

if __name__ == "__main__":
    print("=== Задание 1 ===")
    single_ghost = Ghost("Clyde", "оранжевый", "несмышленый", 5)
    single_ghost.print_info()
    print()

    print("=== Задание 2 ===")
    characters = [
        Ghost("Blinky", "красный", "лидер", 10),
        Ghost("Pinky", "розовый", "устраивает засаду", 7),
        Ghost("Inky", "голубой", "непредсказуемый", 9),
        Ghost("Clyde", "оранжевый", "несмышленый", 5)
    ]

    name = input("Данные о каком персонаже ты хочешь получить? ").strip()
    found = False
    for character in characters:
        if character.nickname.lower() == name.lower():
            character.print_info()
            found = True
            break

    if not found:
        print("Персонаж с таким именем не найден.")
    print()

    print("=== Задание 3 ===")
    pacman = PacMan()

    for _ in range(3): 
        pacman.move()
        pacman.eat_points()
        random.choice(characters).print_string()

    print(f"Итоговые очки Pac-Man: {pacman.points}. Осталось жизней: {pacman.lives}.")
