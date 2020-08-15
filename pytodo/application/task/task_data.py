import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytodo.domain.models import Task


class TaskData:
    __id: uuid.UUID
    __is_done: bool
    __text: str

    def __init__(self, source: "Task") -> None:
        self.__id = source.id.value
        self.__is_done = source.is_done
        self.__text = source.text.value

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def is_done(self) -> bool:
        return self.__is_done

    @property
    def text(self) -> str:
        return self.__text
