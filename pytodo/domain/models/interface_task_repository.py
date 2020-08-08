from abc import abstractmethod
from typing import TYPE_CHECKING, List, Optional, Protocol

if TYPE_CHECKING:
    from pytodo.domain.models.task import Task
    from pytodo.domain.models.task_id import TaskId


class ITaskRepository(Protocol):
    @abstractmethod
    def save(self, task: "Task") -> None:
        ...

    @abstractmethod
    def find(self, id: "TaskId") -> "Optional[Task]":
        ...

    @abstractmethod
    def find_all(self) -> "List[Task]":
        ...

    @abstractmethod
    def delete(self, task: "Task") -> None:
        ...
