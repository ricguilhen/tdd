# task_manager.py
import uuid

class Task:
    """
    Representa uma única tarefa com id, nome, descrição e status.
    Levanta um erro se o nome estiver vazio ou contiver apenas espaços.
    """
    def __init__(self, name, description):
        if not name or not name.strip():
            raise ValueError("O nome da tarefa não pode ser vazio")
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.status = "em andamento"

class TodoList:
    """
    Gerencia a coleção de tarefas, permitindo adicionar, modificar,
    e remover tarefas do dicionário.
    """
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        """Cria e adiciona uma nova tarefa ao dicionário."""
        new_task = Task(name, description)
        self.tasks[new_task.id] = new_task
        return new_task

    def mark_as_completed(self, task_id):
        """Marca uma tarefa como 'concluída'."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada")
        if self.tasks[task_id].status == "concluída":
            raise ValueError("A tarefa já está marcada como concluída")
        self.tasks[task_id].status = "concluída"

    def mark_as_in_progress(self, task_id):
        """Marca uma tarefa como 'em andamento'."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada")
        if self.tasks[task_id].status == "em andamento":
            raise ValueError("A tarefa já está em andamento")
        self.tasks[task_id].status = "em andamento"

    def edit_task(self, task_id, new_name, new_description):
        """Edita o nome e a descrição de uma tarefa existente."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada")
        if not new_name or not new_name.strip():
            raise ValueError("O novo nome da tarefa não pode ser vazio")
        self.tasks[task_id].name = new_name
        self.tasks[task_id].description = new_description
        
    def delete_task(self, task_id):
        """Remove uma tarefa do dicionário."""
        if task_id not in self.tasks:
            raise KeyError("Tarefa não encontrada")
        del self.tasks[task_id]
