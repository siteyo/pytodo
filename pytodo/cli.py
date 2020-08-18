"""
pytodo CLI application module.

It is enabled on the command line using the fire module.

Attributes
----------
DIR: str
    The directory that stores application data, defaults to "~/.pytodo/"
FILENAME: str
    The name of the file that stores the application data, defaults to "data.json"
"""

import os
from typing import TYPE_CHECKING, List, Optional

import fire

from pytodo.application.task import TaskApplicationService, TaskUpdateCommand
from pytodo.domain.models import TaskRepository

if TYPE_CHECKING:
    from pytodo.application.task import TaskData


DIR = "~/.pytodo/"
FILENAME = "data.json"


class CliApp:
    """
    A class that implements the commands that can be used in the pytodo CLI application.
    """

    __task_app_service: TaskApplicationService

    def __init__(self, dir: str = DIR, filename: str = FILENAME) -> None:
        """
        Initialize CLI application.

        Parameters
        ----------
        dir: str
            The directory that stores application data.
        filename: str
            The name of the file that stores the application data.
        """

        self.init(dir, filename)
        repo = TaskRepository(dir, filename)
        self.__task_app_service = TaskApplicationService(repo)

    def init(self, dir: str = DIR, filename: str = FILENAME) -> None:
        """
        Check the existence of the directory and file, and create them if they do not exist.

        Parameters
        ----------
        dir: str
            The directory that stores application data.
        filename: str
            The name of the file that stores the application data.
        """

        path = os.path.expanduser(dir)
        if not os.path.exists(path):
            print(f"{path} is not exist.")
            while True:
                print("Do you want to create a directory?", end="")
                i = input("(Y/n)")
                if i == "n":
                    print("The initialization process has been canceled.")
                    return
                elif i in ["y", "Y", ""]:
                    print(f"Created a directory in '{path}'")
                    os.makedirs(path)
                else:
                    print("Please input 'y' or 'n'")

        options_str = ""
        if dir != DIR:
            options_str += f" --dir={path}"
        if filename != FILENAME:
            options_str += f" --filename={filename}"
        if len(options_str) > 0:
            print()
            print(f"echo alias pytodo='pytodo{options_str}' >> .bash_profile")

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

    def edit(self, index: int, text: Optional[str] = None) -> None:
        """
        Edit task text.

        Parameters
        ----------
        index: int
            Index of task.
        text: str, optional
            New text, defaults to None.
        """
        if text is None:
            text = input("Input new text: ")
        tasks_data: List["TaskData"] = self.__task_app_service.get_all()
        cmd = TaskUpdateCommand(tasks_data[index].id, tasks_data[index].is_done, text)
        self.__task_app_service.update(cmd)


def main() -> None:
    fire.Fire(CliApp)
