from typing import List
from project.task import Task


class Section:
    def __init__(self, name:  str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"Task {task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        if task_name not in [task.name for task in self.tasks]:
            return f"Could not find task with the name {task_name}"
        for task_obj in self.tasks:
            if task_obj.name == task_name:
                task_obj.completed = True
                return f"Completed task {task_obj.name}"

    def clean_section(self):
        removed_task_counter = 0
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_task_counter += 1
        return f"Cleared {removed_task_counter} tasks."

    def view_section(self):
        info = [f'Section {self.name}:']
        for element in self.tasks:
            info.append(element.details())
        return '\n'.join(info)


# Test code:
task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())








