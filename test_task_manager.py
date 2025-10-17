import unittest
# É necessário criar um Enum ou uma classe para os status para este código funcionar
class TaskStatus:
    EM_ANDAMENTO = "em andamento"
    CONCLUIDA = "concluída"

from task_manager import TodoList

class TestCompleteTodoList(unittest.TestCase):

    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task_successfully(self):
        task = self.todo_list.add_task("Comprar pão", "Ir a padaria.")
        self.assertIn(task.id, self.todo_list.tasks)
        self.assertEqual(self.todo_list.tasks[task.id].name, "Comprar pão")
        self.assertEqual(self.todo_list.tasks[task.id].status, TaskStatus.EM_ANDAMENTO)

    def test_add_task_with_empty_name_raises_error(self):
        with self.assertRaises(ValueError):
            self.todo_list.add_task("", "Descrição sem nome")
        with self.assertRaises(ValueError):
            self.todo_list.add_task("   ", "Descrição com espaços")

    def test_mark_task_as_completed(self):
        task = self.todo_list.add_task("Estudar TDD", "Ler documentação")
        self.todo_list.mark_as_completed(task.id)
        self.assertEqual(self.todo_list.tasks[task.id].status, TaskStatus.CONCLUIDA)

    def test_mark_already_completed_task_raises_error(self):
        task = self.todo_list.add_task("Fazer café", "Usar pó :0")
        self.todo_list.mark_as_completed(task.id)
        with self.assertRaises(ValueError):
            self.todo_list.mark_as_completed(task.id)

    def test_mark_task_as_in_progress(self):
        task = self.todo_list.add_task("Passear com o cachorro", "")
        self.todo_list.mark_as_completed(task.id)
        self.todo_list.mark_as_in_progress(task.id)
        self.assertEqual(self.todo_list.tasks[task.id].status, TaskStatus.EM_ANDAMENTO)

    def test_mark_in_progress_if_already_in_progress_raises_error(self):
        task = self.todo_list.add_task("Tarefa inicial", "")
        with self.assertRaises(ValueError):
            self.todo_list.mark_as_in_progress(task.id)

    def test_edit_existing_task(self):
        task = self.todo_list.add_task("Nome Antigo", "Desc Antiga")
        new_name = "Nome Novo"
        new_desc = "Descrição Nova"
        self.todo_list.edit_task(task.id, new_name, new_desc)
        self.assertEqual(self.todo_list.tasks[task.id].name, new_name)
        self.assertEqual(self.todo_list.tasks[task.id].description, new_desc)
        
    def test_edit_non_existent_task_raises_error(self):
        with self.assertRaises(KeyError):
            self.todo_list.edit_task("id-falso", "Nome", "Desc")

    def test_delete_task_successfully(self):
        task = self.todo_list.add_task("Tarefa a ser removida", "")
        self.todo_list.delete_task(task.id)
        self.assertNotIn(task.id, self.todo_list.tasks)

    def test_delete_non_existent_task_raises_error(self):
        with self.assertRaises(KeyError):
            self.todo_list.delete_task("id-falso")

if __name__ == '__main__':
    unittest.main()
