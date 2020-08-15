import uuid
from typing import Callable, List

import pytest

from pytodo.application.task import TaskApplicationService
from pytodo.application.task import TaskData
from pytodo.application.task import TaskUpdateCommand
from pytodo.domain.models import TaskRepository


@pytest.fixture
def task_app_service_factory() -> Callable[[TaskRepository], TaskApplicationService]:
    def factory(repo: TaskRepository) -> TaskApplicationService:
        repo.clear()
        return TaskApplicationService(repo)

    return factory


class TestTaskUpdateCommand:
    def test_cmd(self) -> None:
        u = uuid.uuid1()
        string = "Test string"
        cmd = TaskUpdateCommand(u, string)
        assert cmd.id == u
        assert cmd.text == string


class TestTaskApplicationService:
    def test_init(self, task_repository: TaskRepository) -> None:
        TaskApplicationService(task_repository)

    def test_add(
        self,
        task_repository: TaskRepository,
        task_app_service_factory: Callable[[TaskRepository], TaskApplicationService],
    ) -> None:
        app_service = task_app_service_factory(task_repository)
        app_service.add("Hello")

    def test_update(
        self,
        task_repository: TaskRepository,
        task_app_service_factory: Callable[[TaskRepository], TaskApplicationService],
    ) -> None:
        app_service = task_app_service_factory(task_repository)
        app_service.add("Hello")

    def test_get(
        self,
        task_repository: TaskRepository,
        task_app_service_factory: Callable[[TaskRepository], TaskApplicationService],
    ) -> None:
        app_service = task_app_service_factory(task_repository)
        app_service.add("Hello")
        tasks: List[TaskData] = app_service.get_all()
        assert len(tasks) > 0
        task = app_service.get(tasks[0].id)
        assert task is not None

    def test_get_all(
        self,
        task_repository: TaskRepository,
        task_app_service_factory: Callable[[TaskRepository], TaskApplicationService],
    ) -> None:
        app_service = task_app_service_factory(task_repository)
        app_service.add("Hello")
        tasks: List[TaskData] = app_service.get_all()
        for task in tasks:
            assert isinstance(task, TaskData)

    def test_delete(
        self,
        task_repository: TaskRepository,
        task_app_service_factory: Callable[[TaskRepository], TaskApplicationService],
    ) -> None:
        app_service = task_app_service_factory(task_repository)
        app_service.add("Hello")
        tasks: List[TaskData] = app_service.get_all()
        assert len(tasks) > 0
        app_service.delete(tasks[0].id)
