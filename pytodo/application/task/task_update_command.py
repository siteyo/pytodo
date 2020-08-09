import uuid


class TaskUpdateCommand:
    __id: uuid.UUID
    __text: str

    def __init__(self, id: uuid.UUID, text: str) -> None:
        if not isinstance(id, uuid.UUID):
            raise TypeError
        self.__id = id

        if not isinstance(text, str):
            raise TypeError
        self.__text = text

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def text(self) -> str:
        return self.__text
