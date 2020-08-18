"""
Interface of task repository included in models package.
"""

from abc import abstractmethod
from typing import TYPE_CHECKING, List, Optional, Protocol

if TYPE_CHECKING:
    from .task import Task
    from .task_id import TaskId


class ITaskRepository(Protocol):
    """
    Interface of task's repository.

    Inherit this class and implement abstract method when implementing task repository.
    """

    @abstractmethod
    def save(self, task: "Task") -> None:
        """
        Persist and update task data.

        Parameters
        ----------
        task: Task
            Task model you want to persist
        """

        ...

    @abstractmethod
    def find(self, id: "TaskId") -> "Optional[Task]":
        """
        Find task using task ID.

        Parameters
        ----------
        id: TaskId
            Task ID of task data you want to find.

        Returns
        -------
        Task or None
            Returns the found Task.
            Returns None if not found.
        """

        ...

    @abstractmethod
    def find_all(self) -> "List[Task]":
        """
        Find all task.

        Returns
        -------
        list of Task
            All tasks stored in the repository.
        """

        ...

    @abstractmethod
    def delete(self, task: "Task") -> None:
        """
        Delete persistant task data.

        Parameters
        ----------
        task: Task
            Task model you want to delete.
        """

        ...
