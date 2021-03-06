import uuid
from typing import Callable, List

import pytest

from pytodo.domain.models import Task, TaskId, TaskRepository, Text
from tests.settings import TEST_DIR, TEST_FILENAME


class TestTaskId:
    def test_init(self) -> None:
        u = uuid.uuid1()
        id = TaskId(u)
        assert id.value == u

    def test_init_errors(self) -> None:
        with pytest.raises(TypeError):
            TaskId()

        with pytest.raises(TypeError):
            TaskId(None)

    def test_eq(self, task_ids_factory: Callable[[int], List[TaskId]]) -> None:
        id_num = 2
        ids = task_ids_factory(id_num)

        id = ids[0]
        other = ids[0]
        assert (id == other) is True

        id = ids[0]
        other = ids[1]
        assert (id == other) is False

    def test_ne(self, task_ids_factory: Callable[[int], List[TaskId]]) -> None:
        id_num = 2
        ids = task_ids_factory(id_num)

        id = ids[0]
        other = ids[0]
        assert (id != other) is False

        id = ids[0]
        other = ids[1]
        assert (id != other) is True


class TestText:
    def test_init(self) -> None:
        string = "Test string "
        t = Text(string)
        assert t.value == string

        t.value = string * 2
        assert t.value == string * 2


class TestTask:
    def test_create(self) -> None:
        string = "Hello, Hello"
        text = Text(string)
        task = Task.create(text)
        assert isinstance(task.id, TaskId)
        assert task.is_done is False
        assert task.text.value == string

    def test_init_raises(self) -> None:
        with pytest.raises(TypeError):
            Task.reconstruct(0, True, Text("Hello"))
        with pytest.raises(TypeError):
            Task.reconstruct(uuid.uuid1(), 0, Text("Hello"))
        with pytest.raises(TypeError):
            Task.reconstruct(uuid.uuid1(), True, "Hello")

    def test_reconstruct(self) -> None:
        id = TaskId(uuid.uuid1())
        is_done = True
        text = Text("Reconstruct")
        task = Task.reconstruct(id, is_done, text)
        assert task.id == id
        assert task.text.value == "Reconstruct"
        assert task.is_done is is_done

    def test_property(self) -> None:
        string = "Hello"
        text = Text(string)
        task = Task.create(text)
        task.is_done = True
        task.text = Text(string * 2)
        assert isinstance(task.id, TaskId)
        assert task.is_done is True
        assert task.text.value == string * 2


class TestTaskRepository:
    def test_init(self) -> None:
        TaskRepository(TEST_DIR, TEST_FILENAME)

        with pytest.raises(ValueError):
            TaskRepository("./wrong/path/", "data.json")

    def test_save(
        self,
        task_repository: TaskRepository,
        create_tasks_factory: Callable[[List[str]], List[Task]],
    ) -> None:
        tasks = create_tasks_factory(["Task1", "Task2"])
        task_repository.save(tasks[0])

    def test_find(
        self,
        task_repository: TaskRepository,
        create_tasks_factory: Callable[[List[str]], List[Task]],
    ) -> None:
        tasks: List[Task] = create_tasks_factory(["Task1", "Task2"])
        task_repository.save(tasks[0])
        task_repository.find(tasks[0].id)

    def test_find_all(self, task_repository: TaskRepository) -> None:
        tasks = task_repository.find_all()
        for task in tasks:
            assert isinstance(task, Task)

    def test_delete(self, task_repository: TaskRepository) -> None:
        tasks = task_repository.find_all()
        for task in tasks:
            task_repository.delete(task)
