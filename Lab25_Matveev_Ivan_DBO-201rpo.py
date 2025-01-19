import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='01052003',
        database='test_database'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        print("\n=== ЗАДАНИЕ 3: ВСТАВКА ДАННЫХ ===")
        insert_query = """
        INSERT INTO users (username, email) VALUES
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com'),
        ('Charlie', 'charlie@example.com')
        """
        cursor.execute(insert_query)
        connection.commit()
        print("Данные успешно вставлены в таблицу 'users'!")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\nСодержимое таблицы 'users':")
        for row in rows:
            print(row)
        print("\n=== ЗАДАНИЕ 4: ОБНОВЛЕНИЕ ДАННЫХ ===")
        alter_query = "ALTER TABLE users ADD COLUMN status VARCHAR(20)"
        cursor.execute(alter_query)
        print("Поле 'status' добавлено в таблицу 'users'!")
        update_query = "UPDATE users SET status = 'active' WHERE username = 'Alice'"
        cursor.execute(update_query)
        connection.commit()
        print("Статус пользователя 'Alice' обновлён на 'active'!")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\nСодержимое таблицы 'users' после обновления:")
        for row in rows:
            print(row)
        print("\n=== ЗАДАНИЕ 5: УДАЛЕНИЕ ДАННЫХ ===")
        delete_query = "DELETE FROM users WHERE id = 2"
        cursor.execute(delete_query)
        connection.commit()
        print("Пользователь с id = 2 удалён!")
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("\nСодержимое таблицы 'users' после удаления:")
        for row in rows:
            print(row)
        print("\n=== ЗАДАНИЕ 6: JOIN ДЛЯ ОБЪЕДИНЕНИЯ ТАБЛИЦ ===")
        create_posts_query = """
        CREATE TABLE IF NOT EXISTS posts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            title VARCHAR(255),
            content TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
        """
        cursor.execute(create_posts_query)
        print("Таблица 'posts' успешно создана!")
        insert_posts_query = """
        INSERT INTO posts (user_id, title, content) VALUES
        (1, 'Post 1', 'Content of post 1'),
        (3, 'Post 2', 'Content of post 2'),
        (3, 'Post 3', 'Content of post 3')
        """
        cursor.execute(insert_posts_query)
        connection.commit()
        print("Данные успешно вставлены в таблицу 'posts'!")
        join_query = """
        SELECT posts.title, posts.content, users.username
        FROM posts
        INNER JOIN users ON posts.user_id = users.id
        """
        cursor.execute(join_query)
        rows = cursor.fetchall()
        print("\nПосты с именами пользователей:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Ошибка: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nСоединение с MySQL закрыто")
