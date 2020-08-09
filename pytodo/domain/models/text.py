class Text:
    __value: str

    def __init__(self, value: str) -> None:
        self.value = value

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError
        if not 0 < len(value) <= 50:
            raise ValueError
        self.__value = value
