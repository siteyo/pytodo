import uuid
from typing import Callable, List

import pytest

from pytodo.domain.models.task import Task
from pytodo.domain.models.task_id import TaskId
from pytodo.domain.models.task_repository import TaskRepository
from pytodo.domain.models.text import Text
from tests.settings import TEST_DIR, TEST_FILENAME


@pytest.fixture
def create_tasks_factory() -> Callable[[List[str]], List[Task]]:
    def factory(texts: List[str]) -> List[Task]:
        return [Task.create(Text(text)) for text in texts]

    return factory


@pytest.fixture
def task_ids_factory() -> Callable[[int], List[TaskId]]:
    def factory(num: int) -> List[TaskId]:
        task_ids: List[TaskId] = []
        for idx in range(num):
            task_ids.append(TaskId(uuid.uuid1()))
        return task_ids

    return factory


@pytest.fixture
def task_repository_factory() -> Callable[[str, str], TaskRepository]:
    def factory(save_to: str, filename: str) -> TaskRepository:
        return TaskRepository(save_to, filename)

    return factory


@pytest.fixture
def task_repository() -> TaskRepository:
    return TaskRepository(TEST_DIR, TEST_FILENAME)
