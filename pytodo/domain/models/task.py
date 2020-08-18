"""
Task value object included in models package.
"""

import copy
import uuid
from typing import Optional

from .task_id import TaskId
from .text import Text


class Task:
    """
    Value object with TaskId, completion flag, and text.

    Do not call __init__() directly.
    When creating an instance, you must use a dedicated class method.
    """

    __id: TaskId
    __is_done: bool
    __text: Text

    def __init__(
        self,
        id: Optional[TaskId] = None,
        is_done: Optional[bool] = None,
        text: Optional[Text] = None,
    ) -> None:
        """
        Perform validation check and storage of arguments.

        You can only call it from a class method create or reconstruct.

        Parameters
        ----------
        id: TaskId, optional
            TaskId used for initialization, defaults to None
        is_done: bool, optional
            Completion flag used for initialization, defaults to None
        text: Text, optional
            Text used for initialization, defaults to None

        Raises
        ------
        TypeError
            If the argument type is wrong.
        """

        # Task ID
        if not isinstance(id, TaskId):
            raise TypeError("The id argument must be an instance of TaskId.")
        self.__id = copy.deepcopy(id)

        # Done
        if not isinstance(is_done, bool):
            raise TypeError("The is_done argument must be of type bool.")
        self.is_done = is_done

        # Text
        if not isinstance(text, Text):
            raise TypeError("The text argument must be an instance of Text")
        self.text = copy.deepcopy(text)

    @classmethod
    def create(cls, text: Text) -> "Task":
        """
        This is a classmethod that creates a task instance.

        Parameters
        ----------
        text: Text
            Text to be stored in the created task.

        Returns
        -------
        Task
            Instance of Task.

        Examples
        --------
        >>> task = Task.create(Text("Read the journal."))

        >>> text = Text("Submit a report.")
        >>> task = Task.create(text)
        """

        task_id = TaskId(uuid.uuid1())
        return cls(task_id, False, text)

    @classmethod
    def reconstruct(cls, id: TaskId, is_done: bool, text: Text) -> "Task":
        """
        This is a classmethod that reconstruct a task instance.

        Parameters
        ----------
        id: TaskId

        is_done: bool

        text: Text
            Text to be stored in the created task.

        Returns
        -------
        Task
            Instance of Task.

        Examples
        --------
        """

        return cls(id, is_done, text)

    @property
    def id(self) -> TaskId:
        """
        Property TaskId getter.
        """

        return self.__id

    @property
    def is_done(self) -> bool:
        """
        Property completion flag getter and setter.
        """

        return self.__is_done

    @is_done.setter
    def is_done(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError
        self.__is_done = value

    @property
    def text(self) -> Text:
        """
        Property Text getter and setter.
        """

        return self.__text

    @text.setter
    def text(self, value: Text) -> None:
        if not isinstance(value, Text):
            raise TypeError
        self.__text = copy.deepcopy(value)
