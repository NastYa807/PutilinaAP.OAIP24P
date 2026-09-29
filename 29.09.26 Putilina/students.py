import sqlite3

db = sqlite3.connect("students.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    group_name TEXT NOT NULL,
    grade INTEGER NOT NULL,
    age INTEGER
)
""")

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        ("Путилина Анастасия Павловна", "ИСП-224п", 5, 18)
    )
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        ("Соболева Алена Дмитриевна", "ИСП-224п", 2, 18)
    )
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        ("Салтыкова Виктория Александровна", "ИСП-223а", 3, 19)
    )
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        ("Шмяк Мария Пантелеймоновна", "ОИБ-223а", 5, 19)
    )
    cursor.execute(
        "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
        ("Кузнецов Максим Владимирович", "ИСП-224а", 4, 20)
    )
    db.commit()

while True:
    print("\nМеню:")
    print("1 - Показать всех студентов")
    print("2 - Добавить студента")
    print("3 - Поиск студентов по группе")
    print("4 - Поиск студентов по оценке")
    print("5 - Изменить оценку")
    print("6 - Удалить студента")
    print("7 - Средняя оценка всех студентов")
    print("0 - Выход")

    choice = input("Выберите пункт: ")

    if choice == "1":
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        for student in students:
            print(f"{student[0]}. {student[1]} — {student[2]} — оценка: {student[3]} — возраст: {student[4]}")


    elif choice == "2":
        name = input("Введите ФИО: ")
        group = input("Введите группу: ")
        grade = int(input("Введите оценку: "))
        age = int(input("Введите возраст: "))

        cursor.execute(
            "INSERT INTO students (name, group_name, grade, age) VALUES (?, ?, ?, ?)",
            (name, group, grade, age)
        )
        db.commit()
        print("Студент добавлен")


    elif choice == "3":
        group = input("Введите группу: ")

        cursor.execute(
            "SELECT * FROM students WHERE group_name = ?",
            (group,)
        )

        students = cursor.fetchall()

        for student in students:
            print(f"{student[0]}. {student[1]} — {student[2]} — оценка: {student[3]} — возраст: {student[4]}")


    elif choice == "4":
        grade = int(input("Введите оценку: "))

        cursor.execute(
            "SELECT * FROM students WHERE grade = ?",
            (grade,)
        )

        students = cursor.fetchall()

        for student in students:
            print(f"{student[0]}. {student[1]} — {student[2]} — оценка: {student[3]} — возраст: {student[4]}")


    elif choice == "5":
        student_id = int(input("Введите ID студента: "))
        new_grade = int(input("Введите новую оценку: "))

        cursor.execute(
            "UPDATE students SET grade = ? WHERE id = ?",
            (new_grade, student_id)
        )

        db.commit()
        print("Оценка изменена")


    elif choice == "6":
        student_id = int(input("Введите ID студента: "))

        cursor.execute(
            "DELETE FROM students WHERE id = ?",
            (student_id,)
        )

        db.commit()

        print("Студент удалён( Оставшиеся:")

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()

        for student in students:
            print(f"{student[0]}. {student[1]} — {student[2]} — оценка: {student[3]} — возраст: {student[4]}")


    elif choice == "7":
        cursor.execute("SELECT AVG(grade) FROM students")
        avg = cursor.fetchone()[0]
        print(f"Средняя оценка всех студентов: {avg:.2f}")

    elif choice == "0":
        print("Программа завершена")
        break

    else:
        print("Такого пункта нема")

db.close()
