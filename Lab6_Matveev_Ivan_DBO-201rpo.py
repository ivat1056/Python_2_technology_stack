class Participant:
    def __init__(self, **kwargs):
        self.data = kwargs

    def get_age(self):
        return int(self.data.get('age', 0))

def get_youngest_participant(participants):
    return min(participants, key=lambda x: x.get_age())

def process_orders(**orders):
    total_services = sum(orders.values())
    total_categories = len(orders)
    return total_services, total_categories

print("\nЗадача 1: Участники хакатона")
num_participants = int(input("Введите количество участников: "))
participants = []

for i in range(num_participants):
    print(f"\nВведите данные для участника {i + 1}:")
    name = input("Имя: ")
    surname = input("Фамилия: ")
    age = input("Возраст: ")
    language = input("Язык программирования: ")
    participant = Participant(name=name, surname=surname, age=age, language=language)
    participants.append(participant)

youngest = get_youngest_participant(participants)
print("\nСамый молодой участник:")
for key, value in youngest.data.items():
    print(f"{key}: {value}")

print("\nЗадача 2: Учёт заказов")
orders_data = input("Введите данные о заказах (например, 'Фотосессия=3, Видеосъемка=5'): ")
orders_dict = {item.split('=')[0].strip(): int(item.split('=')[1].strip()) for item in orders_data.split(',')}

total_services, total_categories = process_orders(**orders_dict)
print(f"\nОбщее количество заказанных услуг: {total_services}")
print(f"Количество категорий: {total_categories}")
