import sqlite3;
 
con = sqlite3.connect("metanit.db")
cursor = con.cursor()
 
# обновляем строки, где name = Tom
cursor.execute("DELETE FROM people WHERE name=?", ("Bob",))
con.commit()
 
# проверяем 
cursor.execute("SELECT * FROM people")
print(cursor.fetchall())    # [(1, 'Tomas', 38), (3, 'Sam', 28), (4, 'Alice', 33), (5, 'Kate', 25)]