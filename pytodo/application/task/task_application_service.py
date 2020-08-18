from typing import TYPE_CHECKING, List, Optional

from pytodo.domain.models import ITaskRepository, Task, TaskId, Text

from .task_data import TaskData
from .task_update_command import TaskUpdateCommand

if TYPE_CHECKING:
    import uuid


class TaskApplicationService:
    __task_repository: ITaskRepository

    def __init__(self, task_repository: ITaskRepository):
        self.__task_repository = task_repository

    def add(self, text: str) -> None:
        task = Task.create(Text(text))
        self.__task_repository.save(task)

    def update(self, command: TaskUpdateCommand) -> None:
        target_id = TaskId(command.id)
        task = self.__task_repository.find(target_id)
        if task is None:
            raise ValueError
        text = Text(command.text)
        task.text = text
        task.is_done = command.is_done
        self.__task_repository.save(task)

    def get(self, task_id: "uuid.UUID") -> Optional[TaskData]:
        target_id = TaskId(task_id)
        task = self.__task_repository.find(target_id)
        if task is None:
            return None
        return TaskData(task)

    def get_all(self) -> List[TaskData]:
        tasks = self.__task_repository.find_all()
        tasks_data: List[TaskData] = [TaskData(src) for src in tasks]
        return tasks_data

    def delete(self, task_id: "uuid.UUID") -> None:
        target_id = TaskId(task_id)
        task = self.__task_repository.find(target_id)
        if task is None:
            raise ValueError
        self.__task_repository.delete(task)
