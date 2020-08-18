import copy
import json
import os
import uuid
from typing import Dict, List, Optional, TypedDict

from .interface_task_repository import ITaskRepository
from .task import Task
from .task_id import TaskId
from .text import Text


class TaskData(TypedDict):
    is_done: bool
    text: str


class TaskRepository(ITaskRepository):
    __save_to: str

    def __init__(self, save_to: str, filename: str) -> None:
        expanded_path = os.path.expanduser(save_to)
        if not os.path.exists(expanded_path):
            raise ValueError(expanded_path)

        expanded_path = os.path.expanduser(save_to + filename)
        if not os.path.exists(expanded_path):
            with open(expanded_path, "w") as fp:
                json.dump({}, fp, indent=2)
        self.__save_to = expanded_path

    def __get_all_tasks(self) -> Dict[str, TaskData]:
        with open(self.__save_to, "r") as fp:
            return copy.deepcopy(json.load(fp))

    def save(self, task: Task) -> None:
        tasks = self.__get_all_tasks()
        with open(self.__save_to, "w") as fp:
            tasks.update(
                {str(task.id.value): {"is_done": task.is_done, "text": task.text.value}}
            )
            json.dump(tasks, fp, indent=2)

    def find(self, id: TaskId) -> Optional[Task]:
        todos = self.__get_all_tasks()
        found_task: Optional[Task] = None
        if str(id.value) in todos.keys():
            found_task = Task.reconstruct(
                id, todos[str(id.value)]["is_done"], Text(todos[str(id.value)]["text"]),
            )
        return found_task

    def find_all(self) -> List[Task]:
        task_list: List[Task] = []
        tasks = self.__get_all_tasks()
        for task_id, task_data in tasks.items():
            id = TaskId(uuid.UUID(task_id))
            is_done = task_data.get("is_done", False)
            text = Text(task_data.get("text", ""))
            task = Task.reconstruct(id, is_done, text)
            task_list.append(task)
        return copy.deepcopy(task_list)

    def delete(self, task: Task) -> None:
        tasks = self.__get_all_tasks()
        tasks.pop(str(task.id.value))
        with open(self.__save_to, "w") as fp:
            json.dump(tasks, fp, indent=2)

    def clear(self) -> None:
        with open(self.__save_to, "w") as fp:
            json.dump({}, fp, indent=2)
