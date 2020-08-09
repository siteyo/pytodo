import uuid


class TaskId:
    __value: uuid.UUID

    def __init__(self, value: uuid.UUID) -> None:
        if not isinstance(value, uuid.UUID):
            raise TypeError
        self.__value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TaskId):
            return NotImplemented
        return self.value == other.value

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    @property
    def value(self) -> uuid.UUID:
        return self.__value
