from typing import TYPE_CHECKING, List

import fire

from pytodo.application.task.task_application_service import TaskApplicationService
from pytodo.domain.models.task_repository import TaskRepository

if TYPE_CHECKING:
    from pytodo.application.task.task_data import TaskData


class CliApp:
    __task_app_service: TaskApplicationService

    def __init__(
        self, save_to: str = "~/.pytodo/", filename: str = "data.json"
    ) -> None:
        task_repository = TaskRepository(save_to, filename)
        self.__task_app_service = TaskApplicationService(task_repository)

    def init(self) -> None:
        pass

    def add(self, text: str) -> None:
        self.__task_app_service.add(text)
        print("Added task")

    def list(self) -> None:
        tasks_data: List["TaskData"] = self.__task_app_service.get_all()
        for index, task_data in enumerate(tasks_data):
            print(f"{index}, {task_data.id=}, {task_data.is_done=}, {task_data.text=}")

    def remove(self, index: int) -> None:
        tasks_data: List["TaskData"] = self.__task_app_service.get_all()
        self.__task_app_service.delete(tasks_data[index].id)


def main() -> None:
    fire.Fire(CliApp)
