
class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання додано!")

    def delete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print("Завдання видалено!")
                return
        print("Завдання не знайдено!")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_completed()
                print("Завдання виконано!")
                return
        print("Завдання не знайдено!")

    def show_tasks(self):
        if not self.tasks:
            print("Список завдань порожній!")
            return

        for task in self.tasks:
            status = "Виконано" if task.completed else "Не виконано"
            print(f"\nНазва: {task.name}")
            print(f"Опис: {task.description}")
            print(f"Дедлайн: {task.deadline}")
            print(f"Стан: {status}")


manager = TaskManager()

task1 = Task("Математика", "Виконати вправи", "05.11.2026")
task2 = Task("Англійська", "Вивчити слова", "06.11.2026")

manager.add_task(task1)
manager.add_task(task2)

manager.complete_task("Математика")

manager.show_tasks()

manager.delete_task("Англійська")

manager.show_tasks()
