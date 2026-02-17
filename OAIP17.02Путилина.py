import json
import os


class ProjectManager:
    def __init__(self, filename="projects.json"):
        self.filename = filename
        self.projects = []
        self.load()

    def load(self):
        """Загрузка из JSON"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.projects = json.load(f)

    def save(self):
        """Сохранение в JSON"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.projects, f, ensure_ascii=False, indent=4)

    def show_projects(self):
        print("\n--- Список проектов ---")
        if not self.projects:
            print("Список пуст.")
        else:
            for i, p in enumerate(self.projects):
                print(f"{i + 1}. {p['name']} | Статус: {p['status']} | Задач: {len(p['tasks'])}")

    def get_project_index(self):
        """Вспомогательная функция: выбрать номер проекта"""
        self.show_projects()
        try:
            num = int(input("Введите номер проекта: "))
            if 1 <= num <= len(self.projects):
                return num - 1
            print("Неверный номер.")
            return None
        except:
            print("Нужно ввести число.")
            return None

    def create_project(self):
        name = input("Название проекта: ")
        if name:

            new_project = {
                "name": name,
                "status": "Планирование",
                "tasks": []
            }
            self.projects.append(new_project)
            self.save()
            print("Проект создан!")

    def add_task(self):
        idx = self.get_project_index()
        if idx is not None:
            task = input("Название задачи: ")
            if task:
                self.projects[idx]["tasks"].append(task)
                self.save()
                print("Задача добавлена!")

    def show_tasks(self):
        idx = self.get_project_index()
        if idx is not None:
            print(f"\nЗадачи проекта '{self.projects[idx]['name']}':")
            tasks = self.projects[idx]["tasks"]
            if not tasks:
                print("Задач нет.")
            else:
                for i, t in enumerate(tasks):
                    print(f"{i + 1}. {t}")

    def change_status(self):
        idx = self.get_project_index()
        if idx is not None:
            print("1. Планирование\n2. В работе\n3. Готов")
            choice = input("Выберите статус (1-3): ")
            statuses = {"1": "Планирование", "2": "В работе", "3": "Готов"}

            if choice in statuses:
                self.projects[idx]["status"] = statuses[choice]
                self.save()
                print("Статус обновлен!")
            else:
                print("Неверный выбор.")

    def run(self):
        while True:
            print("\n !МЕНЮ! ")
            print("1. Показать проекты")
            print("2. Создать проект")
            print("3. Добавить задачу")
            print("4. Показать задачи в проекте")
            print("5. Изменить статус проекта")
            print("6. Выход")

            cmd = input("Ваш выбор: ")
            if cmd == "1":
                self.show_projects()
            elif cmd == "2":
                self.create_project()
            elif cmd == "3":
                self.add_task()
            elif cmd == "4":
                self.show_tasks()
            elif cmd == "5":
                self.change_status()
            elif cmd == "6":
                break
            else:
                print("Неверная команда")


if __name__ == "__main__":
    app = ProjectManager()
    app.run()