#Задача: Создай класс `Task`,
# который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи,
# срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.


class Task(): #создаём класс задачи
    def __init__(self, description, due_date, status, ): # вводим характеристики
        self.description = description
        self.due_date = due_date
        self.status = False

class TaskManager:   # создаём класс менеджер задачи.
    def __init__(self):
        self.tasks = []       # создаём список задач

    def add_task(self, description, due_date):  # создаём новую задачу, которая попадает в список
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена.")

    def mark_as_completed(self, description):  #отмечаем выполненную задачу
        for task in self.tasks:
         if task.description == description:
            task.status = True
            print(f"Задача '{description}' отмечена как выполненная.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.is_completed]
        if not current_tasks:
            print("Текущих задач нет.")
            return
        print("Текущие задачи:")
        for task in current_tasks:         #текущие задачи
            print(f"- {task.description}, срок: {task.due_date}")


