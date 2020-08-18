import uuid


class TaskUpdateCommand:
    __id: uuid.UUID
    __is_done: bool
    __text: str

    def __init__(self, id: uuid.UUID, is_done: bool, text: str) -> None:
        if not isinstance(id, uuid.UUID):
            raise TypeError
        self.__id = id

        if not isinstance(is_done, bool):
            raise TypeError
        self.__is_done = is_done

        if not isinstance(text, str):
            raise TypeError
        self.__text = text

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def is_done(self) -> bool:
        return self.__is_done

    @property
    def text(self) -> str:
        return self.__text
