import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',           
        password='01052003' 
    )

    if connection.is_connected():
        cursor = connection.cursor()
        print("=== ЗАДАНИЕ 1: СОЗДАНИЕ БАЗЫ ДАННЫХ ===")
        cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
        print("Успешное соединение и база данных 'test_database' создана!\n")
        connection.database = 'test_database'
        print("=== ЗАДАНИЕ 2: СОЗДАНИЕ ТАБЛИЦЫ ===")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        connection.commit()
        print("Таблица 'users' успешно создана!")

except Error as e:
    print(f"Ошибка: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nСоединение с MySQL закрыто")
