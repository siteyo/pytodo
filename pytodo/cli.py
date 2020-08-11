from typing import TYPE_CHECKING, List

import fire

from pytodo.application.task.task_application_service import TaskApplicationService
from pytodo.domain.models.task_repository import TaskRepository

if TYPE_CHECKING:
    from pytodo.application.task.task_data import TaskData


class CliApp:
    __task_app_service: TaskApplicationService

    def __init__(self) -> None:
        """
        Initialize CLI application.
        """
        app_dir = "~/.pytodo/"
        tasks_file = "data.json"
        repo = TaskRepository(app_dir, tasks_file)
        self.__task_app_service = TaskApplicationService(repo)

    def add(self, text: str) -> None:
        """
        Add task.

        Parameters
        ----------
        text: str
            Task description.
        """
        self.__task_app_service.add(text)
        print("Added task")

    def list(self) -> None:
        """
        Display task list.
        """
        tasks_data: List["TaskData"] = self.__task_app_service.get_all()
        for index, task_data in enumerate(tasks_data):
            disp_text = f"{index}: {task_data.text} - "
            disp_text += "Done" if task_data.is_done else "Not yet"
            print(disp_text)

    def remove(self, index: int) -> None:
        """
        Remove task.

        Parameters
        ----------
        index: int
            Index of task.
        """
        tasks_data: List["TaskData"] = self.__task_app_service.get_all()
        self.__task_app_service.delete(tasks_data[index].id)


def main() -> None:
    fire.Fire(CliApp)
