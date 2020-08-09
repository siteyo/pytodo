import copy
import uuid
from typing import Optional

from pytodo.domain.models.task_id import TaskId
from pytodo.domain.models.text import Text


class Task:
    __id: TaskId
    __is_done: bool
    __text: Text

    def __init__(
        self,
        id: Optional[TaskId] = None,
        is_done: Optional[bool] = None,
        text: Optional[Text] = None,
    ) -> None:
        # Task ID
        if not isinstance(id, TaskId):
            raise ValueError
        self.__id = copy.deepcopy(id)

        # Done
        if not isinstance(is_done, bool):
            raise ValueError
        self.is_done = is_done

        # Contents
        if not isinstance(text, Text):
            raise ValueError
        self.text = copy.deepcopy(text)

    @classmethod
    def create(cls, text: Text) -> "Task":
        task_id = TaskId(uuid.uuid1())
        return cls(task_id, False, text)

    @classmethod
    def reconstruct(cls, id: TaskId, is_done: bool, text: Text) -> "Task":
        return cls(id, is_done, text)

    @property
    def id(self) -> TaskId:
        return self.__id

    @property
    def is_done(self) -> bool:
        return self.__is_done

    @is_done.setter
    def is_done(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError
        self.__is_done = value

    @property
    def text(self) -> Text:
        return self.__text

    @text.setter
    def text(self, value: Text) -> None:
        if not isinstance(value, Text):
            raise TypeError
        self.__text = copy.deepcopy(value)
