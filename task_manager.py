import uuid

class Task:
    def __init__(self, name, description):
        if not name or not name.strip():
            raise ValueError("não pode ser vazio")
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.status = "em andamento"

class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        new_task = Task(name, description)
        self.tasks[new_task.id] = new_task
        return new_task

    def mark_as_completed(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("não encontrada")
        if self.tasks[task_id].status == "concluída":
            raise ValueError("A tarefa já está marcada como concluída")
        self.tasks[task_id].status = "concluída"

    def mark_as_in_progress(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("não encontrada")
        if self.tasks[task_id].status == "em andamento":
            raise ValueError("já está em andamento")
        self.tasks[task_id].status = "em andamento"

    def edit_task(self, task_id, new_name, new_description):
        if task_id not in self.tasks:
            raise KeyError("não encontrada")
        if not new_name or not new_name.strip():
            raise ValueError("não pode ser vazio")
        self.tasks[task_id].name = new_name
        self.tasks[task_id].description = new_description
        
    def delete_task(self, task_id):
        if task_id not in self.tasks:
            raise KeyError("não encontrada")
        del self.tasks[task_id]
