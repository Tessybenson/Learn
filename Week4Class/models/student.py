from .base import Person


class Students(Person):
    def __init__(self, name: str, email: str):
        super().__init__(name, email)

    def addToClass(self, className: str):
        super().addToClass(className)
